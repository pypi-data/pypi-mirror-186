from typing import Generator

import grpc 

from protmo.provide import provide
from protmo.server.user import User
from protmo.db import DB_KEY, Db
from protmo.pm import Message
from protmo.settings_loader import settings
from protmo.utils import *
from typing import Callable
from grpc._server import _RequestIterator
from grpc._server import _Context
from typing import Any
from protmo.pm import _rpc_methods, name_to_grpc_message_or_method # TODO: these two belong somewhere else...

USER_KEY=2

class GenericServicer:
    '''
    Normally with gRPC, you have to implement a servicer for every service-definition
    in your proto-file (which is generarted using the create_proto_file). The idea of
    protmo is, that everyery model defines its @rpc methods freely and can be 
    called by the client. Thus we need one servicer for each model-class. 
    Normally you would implement one for each by hand, but with GenericServicer this 
    is done for you automatically.  
    '''

    def __init__(self, ModelClass):
        self.ModelClass = ModelClass
        self.methods = _collect_methods_of_model_class(ModelClass)

    def __getattribute__(self, name: str) -> type:

        ## Prepare and fetch requied variables for the rest of the method
        #  ==============================================================
        #  They are in the outer scope, as this is done only once. We then return the handler-function
        #  which is called on every request, thus much more often. So keep it lean
        methods = object.__getattribute__(self, 'methods') # set by constructor
        if not name in methods.keys():
            return object.__getattribute__(self, name)
        method = name
        ModelClass = self.ModelClass
        meta = methods[method]
        

        ## Define helper-functions for the handler
        #  =======================================
        #  This method (__getattribute__) is called only once, where the handler is called 
        #  on every request. So define them outside to keep it lean. They are defined as inner methods
        #  to avoid conflicts with __getattribute__ recursions, as __getattribute__ would be called if 
        #  we would call self.wrap_generator(...).
        def wrap_generator(generator: Generator, fn: Callable) -> Generator: # -> Iterator[WhateverFnReturns]
            '''
            Does fn(element) for each element in the Generator. Returns an Generator
            with the results of the fn. It is important to undertand that this can span 
            a long time where the execution is suspended in between. If you don't understand
            this, read up on the yield-python-keyword.
            '''
            for item in generator:
                yield fn(item)

        def extract_requests(request_itertor: _RequestIterator) -> Generator:
            '''
            The gRPC services are called with a self-reference, which is the ID to 
            the current object and becomes the self-pamater in the python-method. 
            The actual request is stored in the request field. This helper extracts
            the actual request-parameter and ignores the self-reference for client-
            side streaming-calls (with Generators).
            '''
            for item in request_itertor:
                yield item.request

        ResultMsg = meta['result_type']
        def wrap_in_result_message(res: Any) -> Any: # -> whatever is in meta['result_type']
            '''
            We can not return raw datatypes directly with gRPC but have to wrap them 
            in a protobuf-message. This method does this while handling edge-cases like
            void or proto-wrapped-in-message.
            '''
            if ResultMsg.__name__ == 'Void':
                return ResultMsg()
            def unwrap(msg):
                if isinstance(msg, Message):
                    msg = msg.proto
                return msg
            if isinstance(res, list):
                res = [unwrap(element) for element in res]
            else:
                res = unwrap(res)
            res = ResultMsg(result=res)
            return res

        ## Create a handler to to handle cient-request
        #  ===========================================
        #  This code is executed when the client calls. It creates the self-reference, the database and the user.
        #  It also handles the paramer-object deconstruction and creation of the result-parameter, so that it is 
        #  compatible with gRPC (which requires exactly one of both). It also manages client- and server-side 
        #  streaming.
        def handler(request: Any, context: _Context) -> Any: # -> A Generator if it is Server Side Streaming or a Protobuf-Message if not.
            '''
            This is called when a new request arrives when the client calls the server. 
            
            The request is either a unary or streaming call, which have to be handled differently and both 
            end in a result. The return is then either a normal return or server-side streaming, which has to be 
            handled differently. This lead to the two ifs in this function. 
            '''
            try:
                
                ## Create the self-reference (first parameter of python-method-calls)
                #  ==================================================================
                instance = ModelClass() # becomes the self-reference of the @rpc-method, e.g. in `def sayHello(self, name)`
                instance._loaded = False # enable lazy loading. The __getattribute__ of Message detecets, that it is false and loads it from the DB, which sets it then to True again
                instance.context = context # the context carries useful stuff for the RPC-method, like the database-connection or the current user
                user = User.from_jwt_userinfo(instance.context.userinfo) if instance.context.userinfo else None
                instance.user = user

                ## Connect to the correct database for the realm
                #  =============================================
                # protmo is multi-tendant per default, which means, that each realm gets its own database
                # This is fully transparent to the client and to the server as well. The database in the context
                # is just connected to the correct database. It is not possible to load wrong data from other 
                # tendants and you have not to worry about multi-tendants. The code is shared, the data not.
                # The Db-instance is later provided and be either accessed via use_provided or via a property
                # in the Message-superclass
                mongo_settings = settings.get('mongodb', {})
                db = Db(
                    mongo_settings.get('host', 'localhost'),
                    mongo_settings.get('port', 27017), 
                    context.realm)
                
                # First if: Uniary call or Client-Side-Streaming
                if isinstance(request, grpc._server._RequestIterator): # streaming call
                    request_iterator = request
                    requests = extract_requests(request_iterator)
                    res = provide({
                        USER_KEY: user,
                        DB_KEY: db
                    }, getattr(instance, method), requests=requests)
                else: # unary call
                    kwargs = {}
                    for field in request.DESCRIPTOR.fields:
                        
                        # We already constructed the self-instance for the method call, but now,
                        # we have to bind the ID from the request to it. Thus search for the 
                        # self-field in the request-proto-message and load the ID (with getattr)
                        if field.name == 'self':
                            instance.id = getattr(request, field.name)
                            instance._id = instance.id
                            continue
                        
                        # extract the values from the message of the call-proto-object and 
                        # add them to the parameter list, which is then used to call the actual
                        # python message. 
                        # Protobuf allows only a single argument, which is an Message. Thus to 
                        # pass multiple arguments, protmo constructs a parameter object as 
                        # a message, for example:
                        #
                        # message EmployeeDoNothingNamedParam {
                        #   string self = 1;
                        #   string name = 2;
                        # }
                        # 
                        # The next line deconstructs this into kwargs, so that we can call the 
                        # python-method with the signature: 
                        # `def doNothingNamed(self, name : str):`
                        kwargs[field.name] = getattr(request, field.name)

                    # here, the actual call to the python-method happens. It is wrapped in 
                    # provice to enable access to the database. The second argument is a pointer 
                    # to the method and all following ones are the parameters to that method.
                    res = provide({DB_KEY: db, USER_KEY: user}, getattr(instance, method), **kwargs)
                


                ## Prepare the result of the @rpc-method for transportation
                #  ========================================================
                # We don't want to construct the Protobuf-Result-Message in our @rpc-method, 
                # but return a raw string for example. We need a result message as we can not 
                # return raw datataypes like string or int32 via gRPC, but need to return a 
                # message, for example `message Result{ string result=1; }`. Also we may want 
                # to add metadata to the result-message as well. Thus we need to wrap the reult
                # from the @rpc-method with it.
                # With server-side streaming, we have to do this whenever the Generator yields
                # a new value, thus we wrap the generator.
                # Second big if: Distiguish between normal retutrn or server-side streaming
                if isinstance(res, Generator): # ServerSide Streaming
                    # handle side server side streaming
                    return wrap_generator(res, wrap_in_result_message)
                else: # Direct Return
                    return wrap_in_result_message(res) 
            
            except Exception as e:
                # don't let any error tear down the server. Catch it, report it and 
                import traceback
                print_sterr(traceback.format_exc())
                print_sterr(e)
            
        return handler


def _collect_methods_of_model_class(ModelClass: type) -> dict:
    '''
    Used by the GenericServer to get the methods of a given ModelClass. A ModelClass is 
    a class defined by the user which extends the Message from `pm.py` and contains multiple
    fields and @rpc-methods. This function extracts the @rpc-methods from the user-defined 
    class. 
    The mechanism is interesting. When the user flags a method with the @rpc-annotation, the 
    code of `def rpc()` is executet, as soon as the file is loaded. Within this code, we add 
    the method to _rpc_methods, so that we can determine in this function, wether a given 
    method is a rpc-method or not.
    '''
    modelName = ModelClass.__name__

    methods = {}
    for attr in dir(ModelClass): # loop over all attributes and see which one are @rpc-methods
        field = getattr(ModelClass, attr)

        # with `field in _rpc_methods.keys()`, we can determine if the method has the @rpc-annotation
        # TODO: I don't know, why `field.__hash__` is here
        if field.__hash__ and field in _rpc_methods.keys(): 
            methodName = field.__name__
            
            # Each gRPC procedure has a Result-object, which is called ModelNameMethodNameResult
            # But we need it as python-reference to the type, so that we can intantiate later in
            # the server, which takes the return of the @rpc-method and wraps it with that message.
            # Therefore construction this name by convention and look up the reference in the 
            # generated protobuf-file we registered via register_pb_module
            result_type = name_to_grpc_message_or_method(f'{modelName}{cap(methodName)}Result')
            if not result_type:
                result_type = name_to_grpc_message_or_method('Void')

            methods[methodName] = {
                'result_type': result_type
            }
    return methods
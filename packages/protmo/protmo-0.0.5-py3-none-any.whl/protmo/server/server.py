from concurrent import futures
import grpc 
from protmo.server.auth_interceptor import AuthInterceptor
from protmo.settings_loader import settings
from protmo.pm import Message
from mypy_extensions import NoReturn
from grpc._server import _Server
from protmo.pm import name_to_grpc_message_or_method
from protmo.utils import *
from protmo.server.generic_servicer import GenericServicer

def run_server() -> NoReturn:
    '''
    You first have to load all modules (as defined in your settings.py) and then
    serve them. This methods helps you with it.
    '''
    load_modules()
    serve()



def load_modules() -> None:
    '''
    The modules are defined in the `settings.py` in the root of the project of the user.
    There is a `modules = [...]` where the folders are listed where the different `models.py`
    are located. This function imports these and by doing that, makes them accessible to 
    `Message.__subclasses__()` which is later used in serve()->_register_models_to_server()
    '''
    modules = settings.modules
    for module in modules:
        __import__(module + '.' + 'models')


def serve() -> NoReturn:
    '''
    Starts a gRPC server with all the Servicers for the differen ModelClasses.
    It is required, that you call load_modules() first in a normal application, or you just
    call `run_server()` which does this for you.
    '''
    interceptors = [AuthInterceptor()]

    # https://stackoverflow.com/questions/55338451/grpc-python-max-workers-limiting-number-of-simultaneous-processes
    # max_workers is the limiting number when streaming is involved. The default is min(32, (os.cpu_count() or 1) + 4), 
    # if we don't set anything
    # We have to implement auto-scaling in the future by ourself
    max_workers = 30 # TODO: pass it via argparse or let it compute
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=max_workers), 
        interceptors=interceptors)
    _register_models_to_server(server)
    port = '[::]:50051'
    server.add_insecure_port(port)
    print(f'listen to {port}')
    server.start()
    server.wait_for_termination()
 
_messages_by_name = {}


def _register_models_to_server(server: _Server) -> None:
    '''
    Registers all available Models at the gRPC-server, so that the client 
    can call the @rpc-methods through gRPC.
    The models are available, because load_modules() loaded them first.
    A Model is a custom class that extends the Message from `pm.py`.
    '''
    for ModelClass in Message.__subclasses__():
        if ModelClass.__name__ in _messages_by_name:
            raise Exception('Duplicate Message ' + ModelClass.__name__)
        _messages_by_name[ModelClass.__name__] = ModelClass
        try:
            _register_model_at_grpc_server(ModelClass, server)
        except AttributeError as e:
            pass # ok, not all Models have Servicers


def _register_model_at_grpc_server(ModelClass: type, server: _Server) -> None:
    '''
    Creates a servicer for the given ModelClass (which is a custom class that extends the 
    message class of `pm.py`) and registers it with the gRPC-Server.
    '''
    servicer = GenericServicer(ModelClass)
    _register_servicer_at_server(ModelClass.__name__, servicer, server)
    

def _register_servicer_at_server(modelName:str, servicer:GenericServicer, server:_Server):
    ## Register the servicer using the gRPC-Genertated method
    #  ======================================================
    # Look at the gRPC-documentation: https://grpc.io/docs/languages/python/basics/
    # To register a servicer to a server, we need to call the grpc-generated method
    # add_<<ServiceName>>Servicer_to_server
    # Thus, we look up this name and get a python-reference to that method and call it
    name = f'add_{modelName}MethodsServicer_to_server'
    grpcServerRegistrationMethod = name_to_grpc_message_or_method(name)
    if not grpcServerRegistrationMethod:
        raise AttributeError(f'{name} not found')
    grpcServerRegistrationMethod(servicer, server)

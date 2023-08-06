import grpc 
from protmo.server.open_id import openid_for_realm
from grpc._server import _Context
from typing import Any
from grpc._server import _HandlerCallDetails
from grpc._utilities import RpcMethodHandler
from typing import Callable
from protmo.server.open_id import OpenIdConnection
from typing import Dict
from protmo.name_to_protobuf import name_to_grpc_message_or_method
from protmo.pm import _rpc_methods


class AuthInterceptor(grpc.ServerInterceptor):

    

    def intercept_service(self, continuation: Callable, handler_call_details: _HandlerCallDetails) -> RpcMethodHandler:
        

        attrs = self._rpc_method_attribues(handler_call_details.method)
        has_to_be_authenticated = True
        if attrs.get('unauthenticated'):
            has_to_be_authenticated = False
        
        def deny(_, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid key')
        self._deny = grpc.unary_unary_rpc_method_handler(deny)

        

        meta = handler_call_details.invocation_metadata
        userinfo = None
        openid = None
        realm = None

        if meta:
            for m in meta:
                if m.key == 'rpc-realm':
                    realm = m.value
                    openid = openid_for_realm(realm)

        if meta and has_to_be_authenticated:
            for m in meta:
                if m.key == 'rpc-auth-header':
                    token = m.value 
                    try:
                        userinfo = self._token_to_userinfo(openid, token)
                    except Exception as e:
                        print(e)
        
        if not userinfo and has_to_be_authenticated:
            return self._deny


        next_handler = continuation(handler_call_details)
        # Returns None if the method isn't implemented.
        if next_handler is None:
            return

        handler_factory, next_handler_method = _get_factory_and_method(next_handler)

        def invoke_intercept_method(request_or_iterator: Any, context: _Context) -> Any:
            context.userinfo = userinfo
            context.realm = realm 
            context.openid = openid
            # method_name = handler_call_details.method
            return next_handler_method(request_or_iterator, context)

        return handler_factory(
            invoke_intercept_method,
            request_deserializer=next_handler.request_deserializer,
            response_serializer=next_handler.response_serializer,
        )

    def _rpc_method_attribues(self, fully_qualified_name):
        from protmo.server.server import _messages_by_name
        _, fully_qualified_message_methods_name, method_name = fully_qualified_name.split('/')
        cls_name = str(fully_qualified_message_methods_name.split('.')[-1]).removesuffix('Methods')
        cls_ptr = _messages_by_name[cls_name]
        method_ptr = getattr(cls_ptr, method_name)
        attributes = _rpc_methods.get(method_ptr)
        return attributes

    def _token_to_userinfo(self, openid: OpenIdConnection, token: str) -> Dict[str, Any]:
        '''
        Decodes a JWT token given by a request and uses the public key of keycloak 
        to verify the signature. The token is base64-encoded and contains a JSON with 
        all the user-info keycloak put there. This method returns this data while 
        checking, that no attacer tinkered with the token (by using the public key and
        signature)
        '''
        options = {"verify_signature": True, "verify_aud": False, "verify_exp": True}
        # takes about 0.5-1.8mx -> MEAN: 1.12ms, STD: 0.56ms
        token_info = openid.openid.decode_token(token, key=openid.public_key, options=options)
        return token_info

def _get_factory_and_method(rpc_handler: grpc.RpcMethodHandler):
    if rpc_handler.unary_unary:
        return grpc.unary_unary_rpc_method_handler, rpc_handler.unary_unary
    elif rpc_handler.unary_stream:
        return grpc.unary_stream_rpc_method_handler, rpc_handler.unary_stream
    elif rpc_handler.stream_unary:
        return grpc.stream_unary_rpc_method_handler, rpc_handler.stream_unary
    elif rpc_handler.stream_stream:
        return grpc.stream_stream_rpc_method_handler, rpc_handler.stream_stream
    else:  # pragma: no cover
        raise RuntimeError("RPC handler implementation does not exist")


class _MyInterceptor(grpc.ServerInterceptor):
    '''
    This is a minimal example of an ServerInterceptor. It uses the continouation
    patterns. They write it is flexible. But it is horrible to use, as you can
    see in the AuthInterceptor. We keep this class to show what is the mininimum
    requirement and give a starting point.
    '''

    def intercept_service(self, continuation, handler_call_details):
        res = continuation(handler_call_details)
        return res
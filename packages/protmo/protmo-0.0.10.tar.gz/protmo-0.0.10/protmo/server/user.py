from __future__ import annotations
from typing import Any
from typing import Dict

class User:
    '''
    The user-object wraps the JSON-data in the JWT which is set
    by keycloak and makes it accessible. The most important method
    reflecting that is the from_jwt_userinfo, where the mapping 
    happens. It is called, whenever a client connects to the server.
    Before anything happens, the AuthInterceptor checks if the JWT
    in the header is valid. Then, User.from_jwt_userinfo is called 
    and the user-instance is set into the context, so that the server
    application-code can access user-info, e.g. to add the users first
    name to a greeting.
    '''

    def __init__(self) -> None:
        self.id = ''
        self.username = ''
        self.email = ''
        self.email_verified = False
        self.realm = ''
        self.firstName = ''
        self.lastName = ''
        self.roles = []
        self.info = ''

    @staticmethod
    def from_jwt_userinfo(userinfo: Dict[str, Any]) -> User:
        '''
        See keycloak and OpenID-connect documentation for the field
        names. Eg. sub means subject and is the user-id. It is also 
        possible to create Protocol Mappers in keycloak to add custom
        user-attributes which you can manage within keycloak.
        '''
        u = User()
        u.id = userinfo.get('sub')
        u.email = userinfo.get('email')
        u.username = userinfo.get('preferred_username')
        u.firstName = userinfo.get('given_name')
        u.lastName = userinfo.get('family_name')
        u.email_verified = userinfo.get('email_verified')
        u.info = userinfo
        return u

    def __str__(self):
        return f'User(id:{self.id},firstName:{self.firstName},lastName:{self.lastName})'

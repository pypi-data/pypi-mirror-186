'''
Different have different realm-settings. For example a client is defined within
a realm name. Or one realm lives on one OpenID-Server like keycloak and the 
other lives on an entierly different server, for example a Google-Server.
This file manages this connections and gives you the connection  for a given 
realm.
'''
from __future__ import annotations
from keycloak import KeycloakOpenID
from protmo.settings_loader import settings

class OpenIdConnection:
    '''
    Contains whatever you need to connect to an OpenID-Endpoint, including the 
    realm and public_key.
    '''

    def __init__(self, realm: str) -> None:
        self.openid = KeycloakOpenID(server_url=settings.keycloak['server_url'],
            client_id=settings.keycloak['client_id'],
            realm_name=realm,
            client_secret_key=settings.keycloak['client_secret'])
        self.public_key = "-----BEGIN PUBLIC KEY-----\n" + self.openid.public_key() + "\n-----END PUBLIC KEY-----"

openid_connections = {}
def openid_for_realm(realm: str) -> OpenIdConnection:
    '''
    A user belongs to a realm. It is possible, that users from different realm
    use the backend (based on protmo). Each realm has an OpenID-connect 
    provider for the user-information. The connection between the realm and 
    the provider is is stored in openid_connections and this function helps to
    look it up. It gives you a connection with for the given realm or creates 
    on one the fly. The connections contains stuff like the public key and 
    whatever you need to connect to an OpenID-Endpoint
    '''
    if not realm in openid_connections:
        openid_connections[realm] = OpenIdConnection(realm)
    return openid_connections[realm]
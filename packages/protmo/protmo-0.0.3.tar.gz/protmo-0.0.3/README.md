proto_model
===========

## Get started with development

- Go to `example`
- Run `docker-compose up`
- Go to [keycloak](http://localhost:8080) and enter
    - username: `skytala`
    - password: `4CAkF5N6sx4b5sJuyFWhw2V3HkdMGjRudMeHAhDWeX`
    - as stated in `example/docker-compose.yaml`
- Create a new realm by importing `realm-export.json`
- Create a new user
    - username: `tom`
    - password: `password`
    - make sure, that the password is not temporal
- make sure, that there are the required certs in `example/certs`, 
    - there should be `tls.crt` and `tls.key`
    - if not, go into `examples` and run `./scripts/create_certificate.sh`. You may need to install mkcert first
- go to example an run
    - `./scripts/start_keycloak.sh`
    - `./scripts/start_mongo.sh`
- append `127.0.0.1 api.example.com` to your `/etc/hosts`

## Run the tests

- Make sure that mongo-db and keycloak are running as described in the section before
- go into the `example` folder and start the server by `python3 run_server.py`
- In the same directory run `./scripts/test.sh`
- You can also go into the root directory and run `./scripts/test.sh` there

## Keycloak/OpenIDConnect Integration

We call keycloak as seldom as possible. To verify a request, we only need the JWT, which is passed by the client and the public key of keycloak, which we fetch only once. Only logging in causes a request every time, which makes sense as we don't store any credentials.

- Logging in works by "forwarding" the login credentials together with the realm to keycloak. This takes about 54ms on localhost
- Fetching the public key of keycloak (for JWT signature validation) happens only once and takes about 5ms on localhost
- Verifing of a JWT happens on within python without a call to keycloak (as we already fetched the public key) and takes on average 1.2ms

## How to register new models

- In the app you are using, create a new folder, e.g. `core`
- create an empty `__init__.py`
- create a `models.py`. The name is important
- In the root of your project, create a `settings.py` with:

```python
modules = [
    'core'
]
```

## How settings work

Here, you also can do other configuration, like: 

```python
import os 

modules = [
    'core'
]

keycloak = {
    'server_url': os.environ['KEYCLOAK_URL'],
    'client_id': os.environ['KEYCLOAK_CLIENT_ID'],
    'client_secret': os.environ['KEYCLOAK_CLIENT_SECRET']
}
```

Now, you access the settings everywhere by:

```python
from proto_model.settings_loader import settings

# ...

settings.keycloak['server_url']
```

Different parts in the systems require specific settings. Look
up in the documentation which are required and append them in the 
`settings.py`.

## Workflow

There are two major phases:
1. Define your model, where you take the stuff from `pm.py` and use it to describe 
   your model, including the available RPC methods
2. Serve, where you start a gRPC-server that takes this model and makes it available
   to clients.

The subsections below describe these steps.

### Define your Model

1. Include and use `pm.py` by extending the `Message` class and using
   the different `Field`s, like `StringField` or `Int32Field`:
    ```python
    class Employee(Message):
        id = StringField(1)
        firstName = StringField(2, default=lambda self: f'no name {self.age}')
        age = Int32Field(3)
    ``` 
2. Take a look in `regen.py`. You use the function `create_proto_file` to 
   create a gRPC-service definition and protobuf-message definition with it.
   This contains the following steps:
   - Locate all loaded subclasses of `Message`
   - Convert each of them to an `MessageInfo` object, which in an AST describing it
   - Use `ModelMessageToProtoMessages` to convert the AST to an protobuf-AST for 
     each message.
   - Use the `str` method on the  elements of the protobuf-AST to generate the code
3. Use protobuf/gRPC to generate the code:
    ```bash
    python3 \
    -m grpc_tools.protoc \
    -I . \
    --python_out=. \
    --grpc_python_out=. \
    proto_model.proto
    ```
4. Start the server with the helper-method `run_server` which first loads (`registerModel`) all available messages (classed that are subclasses of `Message`) in all available modules, which are groupings of messages. Then it calles `serve` to start to serve them. See `server.py` for details.

### Serve

TBD


## Glossary and Definitions

- message
- model
- module 
- server
- gRPC
- protobuf


## Common Errors

- The server is started, but if you send a request from the client, you get `ipv4:127.0.0.1:5443: Failed to connect to remote host: Connection refused`
    - NGINX is not started. It wraps the 50051 of the server and provides TLS-encryption around it at the port 5443


## Todo





All Todos:
- Write proper doc strings
    - https://realpython.com/python-project-documentation-with-mkdocs/
- 100% coverage
- create pip package
- unit-test suite and documentation in code
    - install coverage
    - enforce 100%
    - CI-Pipeline in Git
- Make it easy to use by automating like `manage.py`
- dart model generation
    - AST to gen Dart Model
    - Search
    - State Managment
    - Dart Auto Reconnect
    - Token Refresh
- Pagination, incl. Filter
- Watched Queries
- Complete Queries, later specify what to sync
- Authentication API
- Make returning lists possible: `@rpc def generateRandomGreetings(self) -> list[str]:`
- kubernetes (k3s) deployment

I found these todos in regen.py:
- embedd objects, foreign keys?
- acl
- id-handling, entities and value objects
- stream *args, **kwargs
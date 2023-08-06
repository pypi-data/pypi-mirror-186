from protmo.db import Db, DB_KEY
from protmo.provide import provide
from protmo.create_proto_file import create_proto_file
from protmo.dart_ast import create_dart_file


def regen(db_host, db_port, realm, namespace):
    db = Db(db_host, db_port, realm)

    provide({DB_KEY: db}, create_proto_file, namespace)
    provide({DB_KEY: db}, create_dart_file, namespace)

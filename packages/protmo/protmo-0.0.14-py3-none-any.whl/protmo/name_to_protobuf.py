_name_to_pb_mapping = {}  # String->ProtobufMessage (Message Meta)


def name_to_grpc_message_or_method(name: str):  # -> MessageMeta:
    res = _name_to_pb_mapping.get(str(name))
    # if not res:
    #     print(name, 'not found in', _name_to_pb_mapping.keys())
    return res


def register_pb_module(pb_module):
    for element in dir(pb_module):
        if not element.startswith('_'):
            value = getattr(pb_module, element)
            _name_to_pb_mapping[element] = value

from protmo.pm import *
from protmo.ast import *
from protmo.utils import *
from protmo.settings_loader import settings

class _PythonToDart:

    python_dt_to_dart = {
        float: 'double',
        'float': 'double',
        int: 'int',
        'int': 'int',
        bool: 'bool',
        str: 'String',
        'str': 'String',
        'Void': 'void'
    }

    def __init__(self):
        self.dart_dt_to_python = {}
        for dt in self.python_dt_to_dart:
            self.dart_dt_to_python[self.python_dt_to_dart[dt]] = dt

    def python_datatype_to_dart(self, python_datatype: str) -> str:
        return self.python_dt_to_dart.get(python_datatype, python_datatype)

    def dart_datatype_to_python(self, dart_datatype: str) -> str:
        return self.dart_dt_to_python[dart_datatype]


_python_to_dart = _PythonToDart()


class AstToDartAst:

    def __init__(self, ast: MessageInfo):
        self.ast = ast
        self.name = ast.name
        self.methods = [self._to_method(ast, m) for m in ast.rpc_methods]

    def _to_method(self, ast: MessageInfo, rpc_method: Method):
        if rpc_method.clientSideStreaming and rpc_method.serverSideStreaming:
            return BidirectionalStreamingMethod(ast, rpc_method)
        if rpc_method.clientSideStreaming:
            return ClientSideStreamingMethod(ast, rpc_method)
        if rpc_method.serverSideStreaming:
            return ServerSideStreamingMethod(ast, rpc_method)
        return UnaryCallMethod(ast, rpc_method)

    @property
    def should_be_included(self) -> bool:
        return bool(self.methods)

    def __str__(self):
        methods = '\n\n'.join([str(m) for m in self.methods])
        return f'extension {self.name}Rpc on {self.name} {{\n{methods}\n}}\n'


def dart_type(python_type, repeated=False):
    res = _python_to_dart.python_datatype_to_dart(python_type)
    if repeated:
        res = f'List<{res}>'
    return res


class UnaryCallMethod:

    def __init__(self, message: MessageInfo, ast_method: Method):
        self.ast = message
        self.method = ast_method
        self.name = ast_method.name

    def __str__(self):
        returnType = dart_type(
            self.method.returnType.python_type,
            self.method.returnType.repeated)
        param_obj = f'{self.ast.name}{cap(self.name)}Param'
        if self.method.no_params:
            param_obj = 'Void'

        res_assignment = 'final res = ' if not self.method.is_void else ''
        static = 'static ' if self.method.is_static else ''
        res = f'''    {static}Future<{returnType}> {self.name}({self._parameter_list}) async {{
        {res_assignment}await client<{self.ast.name}MethodsClient>()
            .{self.name}({param_obj}({self._param_bindings(self.method.is_static)}));\n'''
        if not self.method.is_void:
            res += '        return res.result;\n'
        res += '    }'

        return res

    def _param_bindings(self, is_static):
        self_ref = ['self: id'] if not is_static else []
        return ', '.join(
            self_ref + [f'{param.name}: {param.name}' for param in self.method.parameters])

    @property
    def _parameter_list(self):
        ast_params = self.method.parameters
        if not ast_params:
            return ''
        inner = ', '.join(
            f'required {dart_type(param.pythonType, param.repeated)} {param.name}' for param in ast_params)
        return f'{{{inner}}}'


class ClientSideStreamingMethod:

    def __init__(self, message: MessageInfo, ast_method: Method):
        self.ast = message
        self.method = ast_method
        self.name = ast_method.name

    def __str__(self):
        returnType = dart_type(
            self.method.returnType.python_type,
            self.method.returnType.repeated)
        param_obj = f'{self.ast.name}{cap(self.name)}Param'
        if self.method.no_params:
            param_obj = 'Void'

        res_assignment = 'final res = ' if not self.method.is_void else ''
        static = 'static ' if self.method.is_static else ''
        self_ref = 'self: id, ' if not self.method.is_static else ''

        res = f'''    {static}Future<{returnType}> {self.name}({self._parameter_list}) async {{
        {res_assignment}await client<{self.ast.name}MethodsClient>()
            .{self.name}(requests.map((request) => {param_obj}({self_ref}request: request)));\n'''
        if not self.method.is_void:
            res += '        return res.result;\n'
        res += '    }'

        return res

    def _param_bindings(self, is_static):
        self_ref = ['self: id'] if not is_static else []
        return ', '.join(
            self_ref + [f'{param.name}: {param.name}' for param in self.method.parameters])

    @property
    def _parameter_list(self):
        ast_params = self.method.parameters
        if not ast_params:
            return ''
        param = ast_params[0]
        return f'Stream<{dart_type(param.pythonType, param.repeated)}> requests'


class ServerSideStreamingMethod:

    def __init__(self, message: MessageInfo, ast_method: Method):
        self.ast = message
        self.method = ast_method
        self.name = ast_method.name

    def __str__(self):
        returnType = dart_type(
            self.method.returnType.python_type,
            self.method.returnType.repeated)
        param_obj = f'{self.ast.name}{cap(self.name)}Param'
        if self.method.no_params:
            param_obj = 'Void'

        res_assignment = 'final res = ' if not self.method.is_void else ''
        static = 'static ' if self.method.is_static else ''
        res = f'''    {static}Stream<{returnType}> {self.name}({self._parameter_list}) {{
        final incoming = client<{self.ast.name}MethodsClient>().{self.method.name}(
            {param_obj}({self._param_bindings(self.method.is_static)}));
        return incoming.map((event) => event.result);\n'''
        res += '    }'

        return res

    def _param_bindings(self, is_static):
        self_ref = ['self: id'] if not is_static else []
        return ', '.join(
            self_ref + [f'{param.name}: {param.name}' for param in self.method.parameters])

    @property
    def _parameter_list(self):
        ast_params = self.method.parameters
        if not ast_params:
            return ''
        inner = ', '.join(
            f'required {dart_type(param.pythonType, param.repeated)} {param.name}' for param in ast_params)
        return f'{{{inner}}}'


class BidirectionalStreamingMethod:

    def __init__(self, message: MessageInfo, ast_method: Method):
        self.message = message
        self.method = ast_method

    def __init__(self, message: MessageInfo, ast_method: Method):
        self.ast = message
        self.method = ast_method
        self.name = ast_method.name

    def __str__(self):
        returnType = dart_type(
            self.method.returnType.python_type,
            self.method.returnType.repeated)
        param_obj = f'{self.ast.name}{cap(self.name)}Param'
        if self.method.no_params:
            param_obj = 'Void'

        res_assignment = 'final res = ' if not self.method.is_void else ''
        static = 'static ' if self.method.is_static else ''
        self_ref = 'self: id, ' if not self.method.is_static else ''

        res = f'''    {static}Stream<{returnType}> {self.name}({self._parameter_list}) {{
        final incoming = client<{self.ast.name}MethodsClient>()
            .{self.name}(requests.map((request) => {param_obj}({self_ref}request: request)));
        return incoming.map((event) => event.result);\n'''
        res += '    }'

        return res

    @property
    def _parameter_list(self):
        ast_params = self.method.parameters
        if not ast_params:
            return ''
        param = ast_params[0]
        return f'Stream<{dart_type(param.pythonType, param.repeated)}> requests'


def create_dart_file(package: str):
    content = '''import 'auth.dart';
import 'client.dart';
import 'package:grpc/grpc.dart';
import 'models.pbgrpc.dart';

'''
    messages: list[MessageInfo] = []
    for model_class in (Message.__subclasses__()):
        msg = MessageInfo(model_class)
        messages.append(msg)

    for msg in messages:
        ast = AstToDartAst(msg)
        if ast.should_be_included:
            content += str(ast) + '\n\n'

    content += '\n\nregisterRpcClients(ClientChannel channel, String token) {\n'
    for msg in messages:
        if msg.has_methods:
            content += f'    registerClient({msg.name}MethodsClient(channel, interceptors: [AuthInterceptor(token)]));\n'
    content += '}\n'

    # registerRpcClients(ClientChannel channel, String token) {
    # registerClient(EmployeeMethodsClient(channel, interceptors: [AuthInterceptor(token)]));
    # }

    with open(settings.dart_proto_folder + '/rpc_methods.dart', 'w') as f:
        f.write(content)

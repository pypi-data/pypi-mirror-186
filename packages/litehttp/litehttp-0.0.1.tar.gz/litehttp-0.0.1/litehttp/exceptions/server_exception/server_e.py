from litehttp.exceptions.server_exception.base_web_exception import BaseServerWebException
from litehttp.exceptions.baseexception import LitehttpBaseException


class PathNotFoundWeb(BaseServerWebException):
    def __init__(self, func_name: str, path: str):
        super().__init__('404', func_name, f'path "{path}" not found')


class ServerTemplateErrorWeb(BaseServerWebException):
    def __init__(self, func_name: str):
        super().__init__('500', func_name, 'server template error')


class TemplateNotFound(BaseServerWebException):
    def __init__(self, func_name: str):
        super().__init__('404', func_name, 'template not found')


class RenderFileDataTypeError(BaseServerWebException):
    def __init__(self, func_name: str):
        super().__init__('500', func_name, 'File type is not a byte.')


class SetHandlersError(LitehttpBaseException):
    def __init__(self, func_name: str):
        super().__init__(func_name, 'The set method must accept at least one handler.')

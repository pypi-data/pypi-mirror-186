from .webserver import FileRender
from .request_obj import Request
from abc import ABCMeta, abstractmethod


class BaseResponse(metaclass=ABCMeta):
    def __init__(self, request: Request):
        self.f_render = FileRender(request.response)

    @abstractmethod
    def response(self) -> list[bytes]:
        pass


class HtmlResponse(BaseResponse):
    def __init__(self, request: Request):
        super().__init__(request)

    def response(self, html_data: str):
        return self.f_render.html_file_render(html_data)


class HtmlFileResponse(BaseResponse):
    def __init__(self, request: Request):
        super().__init__(request)

    def response(self, filepath):
        return self.f_render.file_render(filepath)


class RedirectResponse(BaseResponse):
    def __init__(self, request: Request):
        super().__init__(request)

    def response(self, url):
        return self.f_render.html_file_render('.', code='302 Found', header=['Location', url])

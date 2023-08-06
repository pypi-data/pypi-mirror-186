import os
from wsgiref import util
from dataclasses import dataclass
import mimetypes
from litehttp.exceptions.server_exception.server_e import TemplateNotFound, RenderFileDataTypeError, PathNotFoundWeb, \
    SetHandlersError
from .route.routing import UrlCollectorGet, UrlCollectorPost, MiddlewareCollector, CompareUrlsIdentity
from conf.project import STATICFILES_PATH
from .request_obj import Request
from .middlewares import Middleware
from typing import Type
from cgi import FieldStorage



@dataclass
class RespondValue:
    code: str
    header: list


class Server:
    def __init__(self):
        self.environ = None
        self.respond = None
        self.full_url = None
        self.f_render: FileRender = None
        self.url_route_path = None
        self.url_collector_get = UrlCollectorGet()
        self.url_collector_post = UrlCollectorPost()
        self.middleware_collector = MiddlewareCollector()
        self.request: Request = None

    def start(self, environ, respond) -> list[bytes] | util.FileWrapper:
        self.environ = environ
        self.respond = respond
        self.f_render = FileRender(respond)
        self.full_url = '/' + util.request_uri(self.environ).replace(util.application_uri(self.environ), '')
        self.url_route_path = '/' + util.shift_path_info(self.environ)
        self.request = Request(self.respond)
        self.request.set_url(self.full_url)
        return self._request_method_definition()

    def _request_method_definition(self) -> list[bytes] | util.FileWrapper:
        """
        Determines which method was used by the user. In accordance with the method calls it.
        :return: list[bytes] | util.FileWrapper
        """
        match self.environ['REQUEST_METHOD']:
            case 'GET':
                return self.get_method()
            case 'POST':
                return self.post_method()

    def _get_page_files_path(self, url: str, static_files_path: list[str]) -> str:
        for static_file_p in static_files_path:
            p = url.find(static_file_p)
            if p != -1:
                return url[p:]

    def get_method(self) -> list[bytes] | util.FileWrapper:
        mddl_res = self.run_after_middlewares()
        if mddl_res:
            return mddl_res

        # render page files. Css, js, img, ...
        if self.full_url != '/favicon.ico' and self.full_url.rfind('.') != -1:
            path = self._get_page_files_path(self.full_url, STATICFILES_PATH)
            return self.f_render.file_render(path)

        # render html
        for route_path in list(self.url_collector_get.path.keys()):
            compare_urls = CompareUrlsIdentity(self.full_url, route_path)
            if self.full_url != '/favicon.ico' and compare_urls.compare():
                if compare_urls.is_slug_url():
                    # set url args
                    self.request.set_url_arguments(**{compare_urls.slug_name: compare_urls.slug_value})
                self.run_before_middlewares()
                return self.url_collector_get.path[route_path](self.request)

        # if path not found
        return self.f_render.html_file_render(PathNotFoundWeb('Server.get_method', self.full_url).for_web(),
                                              code="404 Not found")

    def post_method(self):
        for route_path in list(self.url_collector_get.path.keys()):
            compare_urls = CompareUrlsIdentity(self.full_url, route_path)
            if self.full_url != '/favicon.ico' and compare_urls.compare():
                self.request.set_form_data(self.parse_post_data(self.environ))
                return self.url_collector_post.path[route_path](self.request)

        return self.f_render.html_file_render(PathNotFoundWeb('Server.get_method', self.full_url).for_web(),
                                              code="404 Not found")

    def parse_post_data(self, env) -> FieldStorage:
        form_data = FieldStorage(fp=env['wsgi.input'], environ=env, keep_blank_values=True)
        return form_data

    def get(self, url, handler):
        self.url_collector_get.append(url, handler)

    def post(self, url, handler):
        self.url_collector_post.append(url, handler)

    def set(self, url, get_handler, post_handler):
        if get_handler:
            self.url_collector_get.append(url, get_handler)
        if post_handler:
            self.url_collector_post.append(url, post_handler)
        if not get_handler and not post_handler:
            raise SetHandlersError("Server.set")

    def middleware(self, middleware: Type[Middleware]):
        self.middleware_collector.append(middleware)

    def run_after_middlewares(self):
        for mddl in self.middleware_collector.middlewares:
            mddl_res = mddl(self.request).after_response()
            if mddl_res:
                return mddl_res

    def run_before_middlewares(self):
        for mddl in self.middleware_collector.middlewares:
            mddl(self.request).before_response()


class FileRender:
    """
    Rendering of any template files.
    Does not depend on the server and its implementation.
    """
    def __init__(self, respond):
        self.respond = respond

    def __render_file_by_path(self, path: str, respond_value: RespondValue) -> util.FileWrapper:
        """
        Rendering a file at its path.
        """
        self.respond(str(respond_value.code), [respond_value.header])
        file = os.path.join(os.getcwd(), path)
        if os.path.exists(file):
            return util.FileWrapper(open(file, "rb"))

    def __render_file_by_file_data(self, file_data: str, respond_value: RespondValue) -> bytes | None:
        """
        Rendering a file based on its data. Most commonly used for HTML.
        """
        if file_data and isinstance(file_data, str):
            self.respond(str(respond_value.code), [respond_value.header])
            return bytes(file_data, 'utf-8')
        else:
            return None

    def file_render(self, filepath, header: list[str] = None) -> util.FileWrapper | None | list[bytes]:
        """
        Rendering of any file at its address.
        """
        if os.path.exists(os.path.join(os.getcwd(), filepath)):
            mime_type = mimetypes.guess_type(filepath)[0]
            r_header = ["Content-Type", mime_type]
            if header:
                r_header = header
            return self.__render_file_by_path(filepath, RespondValue('200 OK', r_header))
        else:
            return [self.__render_file_by_file_data(TemplateNotFound('_FileRender.file_render').for_web(),
                                                    RespondValue('404 Not Found', ["Content-Type", 'text/html']))]

    def html_file_render(self, html_str_data: str, code: str = None, header: list[str] = None) -> list[bytes]:
        """
        Render template by HTML code.
        """
        mime_type = 'text/html'
        r_header = ["Content-Type", mime_type]
        if header:
            r_header = header
        if not code:
            code = '200 OK'
        file = [self.__render_file_by_file_data(html_str_data, RespondValue(code, r_header))]
        if file[0]:
            return file
        else:
            return [self.__render_file_by_file_data(RenderFileDataTypeError('_FileRender.html_file_render').for_web(),
                                                    RespondValue('404 Not Found', ["Content-Type", 'text/html']))]

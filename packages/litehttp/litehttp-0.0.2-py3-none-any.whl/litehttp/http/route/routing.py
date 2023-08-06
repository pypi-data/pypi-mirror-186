from litehttp.http.middlewares import Middleware
from typing import Type


class UrlCollectorGet:
    def __init__(self):
        self.path = {}

    def append(self, url, handler):
        self.path[url] = handler


class UrlCollectorPost:
    def __init__(self):
        self.path = {}

    def append(self, url, handler):
        self.path[url] = handler


class MiddlewareCollector:
    def __init__(self):
        self.middlewares: list[Type[Middleware]] = []

    def append(self, middleware: Type[Middleware]):
        self.middlewares.append(middleware)


class CompareUrlsIdentity:
    def __init__(self, current_path: str, route_path: str):
        self.current_path = current_path
        self.route_path = route_path
        self.slug_value = ''
        self.slug_name = ''
        self._start = -1
        if self.is_slug_url():
            self._start = self.route_path.find('<')
            self.slug_value = self.get_slug_value()
            self.slug_name = self.get_name()
            self.new_route_path = self._get_new_route_path()
        else:
            self.new_route_path = self.route_path

    def compare(self) -> bool:
        if self.new_route_path == self.current_path:
            return True
        else:
            return False

    def _get_new_route_path(self):
        if self._start != -1:
            end = self.route_path.rfind('>') + 1
            tag = self.route_path[self._start:end]
            rp = self.route_path.replace(tag, self.slug_value)
            return rp

    def get_name(self):
        if self._start != -1:
            end = self.route_path.rfind('>') + 1
            name = self.route_path[self._start + 1:end - 1]
            return name

    def is_slug_url(self):
        if self.route_path.find('<') != -1:
            return True
        else:
            return False

    def get_slug_value(self):
        if self._start != -1:
            left_v: str = self.current_path[self._start:]
            if left_v.find('/') != -1:
                value = left_v[:left_v.find('/')]
            else:
                value = left_v
            return value


if __name__ == '__main__':
    u = 'url/test/wdw'
    u2 = 'url/test/wdw'
    print(CompareUrlsIdentity(u2, u).compare())

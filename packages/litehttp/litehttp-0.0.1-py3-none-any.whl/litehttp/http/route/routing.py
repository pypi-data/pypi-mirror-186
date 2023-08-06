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

from abc import abstractmethod, ABCMeta


class Middleware(metaclass=ABCMeta):
    def __init__(self, request):
        self.request = request

    @abstractmethod
    def after_response(self) -> list[bytes] | None:
        pass

    @abstractmethod
    def before_response(self):
        pass

from litehttp.exceptions.baseexception import LitehttpBaseException


class BaseServerWebException(LitehttpBaseException):
    def __init__(self, code: str, func_name: str, text: str):
        self.code = code
        super().__init__(func_name, text)

    def __str__(self):
        return f'<h2>{self.code} | {self.func_name}: {self.text}</h2>'

    def for_web(self) -> str:
        return f'<h2>{self.code} | {self.func_name}: {self.text}</h2>'

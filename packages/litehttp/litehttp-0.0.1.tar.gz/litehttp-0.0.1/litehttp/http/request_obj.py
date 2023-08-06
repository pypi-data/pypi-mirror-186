class Request:
    def __init__(self, response):
        self.response = response
        self.url = ''

    def set_url(self, url: str):
        self.url = url

from http_request import HttpRequest
from handler import Handler


class WebServer:
    def __init__(self, handler: Handler) -> None:
        self.handler = handler

    def handle(self, request: HttpRequest):
        self.handler.handle(request)
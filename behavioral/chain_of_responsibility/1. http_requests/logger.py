from http_request import HttpRequest
from handler import Handler


class Logger(Handler):
    def __init__(self, next: Handler) -> None:
        super().__init__(next)

    def do_handle(self, request: HttpRequest) -> bool:
        print("Log")
        return False
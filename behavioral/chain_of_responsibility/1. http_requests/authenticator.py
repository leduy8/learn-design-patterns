from http_request import HttpRequest
from handler import Handler


class Authenticator(Handler):
    def __init__(self, next: Handler) -> None:
        super().__init__(next)

    def do_handle(self, request: HttpRequest) -> bool:
        print("Authentication")
        return not (request.get_username() == "admin" and request.get_password() == "1234")
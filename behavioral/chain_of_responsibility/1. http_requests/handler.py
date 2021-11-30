from abc import ABC, abstractmethod
from http_request import HttpRequest


class Handler(ABC):
    def __init__(self, next) -> None:
        super().__init__()
        self.next = next

    def handle(self, request: HttpRequest):
        if self.do_handle(request):
            return

        if self.next is not None:
            self.next.handle(request)


    @abstractmethod
    def do_handle(self, request: HttpRequest) -> bool:
        pass
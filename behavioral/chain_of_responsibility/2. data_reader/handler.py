from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next) -> None:
        self.next = next

    def handle(self, request):
        if self.do_handle(request):
            return

        if self.next is not None:
            self.next.handle(request)

    @abstractmethod
    def do_handle(self, request):
        pass
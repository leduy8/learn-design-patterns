from abc import ABC, abstractmethod


class System:
    def check(self):
        print('Checking...')


class Window(ABC):
    def __init__(self) -> None:
        self.system = System()

    def close(self):
        self.system.check()
        self._do_close()

    @abstractmethod
    def _do_close(self):
        pass


class NormalWindow(Window):
    def _do_close(self):
        print('Closing normal window...')


class SecuredWindow(Window):
    def _do_close(self):
        print('Closing secured window...')


normal = NormalWindow()
normal.close()
secured = SecuredWindow()
secured.close()
from handler import Handler


class NumberFormat(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self, request):
        print('Handle number data...')
        return False
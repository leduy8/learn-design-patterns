from handler import Handler


class QuickbookFormat(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self, request):
        print('Handle quickbook data...')
        return False
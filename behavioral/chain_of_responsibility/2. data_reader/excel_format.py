from handler import Handler


class ExcelFormat(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self, request):
        print('Handle excel data...')
        return False
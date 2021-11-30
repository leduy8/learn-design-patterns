from handler import Handler


class DataReader(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self, request):
        print('Start data reader application...')
        return False
from observer import Observer


class SpreadSheet(Observer):
    def __init__(self, data_source) -> None:
        self.data_source = data_source

    def update(self):
        print(f'Spreadsheet got notified: {self.data_source.get()}')
from observer import Observer


class SpreadSheet(Observer):
    def update(self, value):
        print(f'Spreadsheet got notified: {value}')
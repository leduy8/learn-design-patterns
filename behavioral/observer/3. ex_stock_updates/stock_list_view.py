from observer import Observer


class StockListView(Observer):
    def __init__(self, data_source) -> None:
        self.data_source = data_source

    def update(self):
        print('=================================')
        print(f'Stock update!')
        self.data_source.get_stocks()

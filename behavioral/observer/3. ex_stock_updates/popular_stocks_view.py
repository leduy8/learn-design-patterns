from observer import Observer


class PopularStocksView(Observer):
    def __init__(self, data_source) -> None:
        self.data_source = data_source

    def update(self):
        print('=================================')
        print(f'Popular stocks update!')
        self.data_source.get_popular_stocks()
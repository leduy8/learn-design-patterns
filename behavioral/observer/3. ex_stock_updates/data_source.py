from subject import Subject


class DataSource(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.stocks = []
        self.popular_stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def set_stock(self, stock, value):
        index = self.stocks.index(stock)
        self.stocks[index].set(value)
        super().notify_observers()

    def get_stocks(self):
        for stock in self.stocks:
            stock.print()

    def get_popular_stocks(self):
        temp = sorted(self.stocks, key=lambda x: x.get(), reverse=True)
        self.popular_stocks = temp[0:3]
        for stock in self.popular_stocks:
            stock.print()
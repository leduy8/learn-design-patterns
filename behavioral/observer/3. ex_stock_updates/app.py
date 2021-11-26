from data import AmazonStock, AppleStock, FacebookStock, GoogleStock
from data_source import DataSource
from popular_stocks_view import PopularStocksView
from stock_list_view import StockListView

amazon = AmazonStock(3580.41)
apple = AppleStock(161.94)
facebook = FacebookStock(341.06)
google = GoogleStock(2922.40)

data_source = DataSource()
data_source.add_stock(amazon)
data_source.add_stock(apple)
data_source.add_stock(facebook)
data_source.add_stock(google)

popular_stocks_view = PopularStocksView(data_source)
stock_list_view = StockListView(data_source)

data_source.add_observer(stock_list_view)
data_source.add_observer(popular_stocks_view)

print('Initial stock price: ')
data_source.get_stocks()

print('=================================')

print('Initial popular stocks: ')
data_source.get_popular_stocks()

print('=================================')
print('Update google stock to 59.99')
data_source.set_stock(google, 59.99)
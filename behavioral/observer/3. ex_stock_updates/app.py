from data import AmazonStock, AppleStock, FacebookStock, GoogleStock
from data_source import DataSource
from popular_stocks_view import PopularStocksView
from stock_list_view import StockListView

amazon = AmazonStock()
apple = AppleStock()
facebook = FacebookStock()
google = GoogleStock()

data_source = DataSource()
data_source.add_stock(amazon)
data_source.add_stock(apple)
data_source.add_stock(facebook)
data_source.add_stock(google)

popular_stocks_view = PopularStocksView(data_source)
stock_list_view = StockListView(data_source)

data_source.add_observer(stock_list_view)
data_source.add_observer(popular_stocks_view)

print('Update google stock to 2922.40')
data_source.set_stock(google, 2922.40)

print('=================================')

print('Update amazon stock to 3580.41')
data_source.set_stock(amazon, 3580.41)

print('=================================')

print('Update facebook stock to 341.06')
data_source.set_stock(facebook, 341.06)

print('=================================')

print('Update apple stock to 161.94')
data_source.set_stock(apple, 161.94)

print('=================================')

print('Update amazon stock to 59.99')
data_source.set_stock(amazon, 59.99)
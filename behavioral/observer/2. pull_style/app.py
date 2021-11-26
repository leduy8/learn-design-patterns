from chart import Chart
from spread_sheet import SpreadSheet
from data_source import DataSource


data_source = DataSource()
sheet1 = SpreadSheet(data_source)
sheet2 = SpreadSheet(data_source)
chart = Chart(data_source)

data_source.add_observer(sheet1)
data_source.add_observer(sheet2)
data_source.add_observer(chart)
data_source.set(69)
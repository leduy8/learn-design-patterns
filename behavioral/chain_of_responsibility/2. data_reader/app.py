from excel_format import ExcelFormat
from number_format import NumberFormat
from quickbook_format import QuickbookFormat
from data_reader import DataReader

excel = ExcelFormat(None)
number = NumberFormat(excel)
quickbook = QuickbookFormat(number)
reader = DataReader(quickbook)
reader.handle(None)
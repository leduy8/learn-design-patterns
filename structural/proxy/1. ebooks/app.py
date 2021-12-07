from library import Library
from ebook_proxy import EbookProxy
from logging_ebook_proxy import LoggingEbookProxy


lib = Library()
filenames = ['a', 'b', 'c']
for filename in filenames:
    lib.add(LoggingEbookProxy(filename))

lib.open_ebook('a')
lib.open_ebook('b')
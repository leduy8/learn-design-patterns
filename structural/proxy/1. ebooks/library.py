from ebook import Ebook


class Library:
    def __init__(self) -> None:
        self.ebooks = {}

    def add(self, ebook: Ebook):
        self.ebooks[ebook.get_filename()] = ebook

    def open_ebook(self, filename):
        self.ebooks[filename].show()
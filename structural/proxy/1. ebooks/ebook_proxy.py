from ebook import Ebook
from real_ebook import RealEbook


class EbookProxy(Ebook):
    def __init__(self, filename) -> None:
        self.filename = filename
        self.ebook = None

    def show(self):
        if self.ebook is None:
            self.ebook = RealEbook(self.filename)
        
        self.ebook.show()

    def get_filename(self):
        return self.filename
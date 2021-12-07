from ebook import Ebook


class RealEbook(Ebook):
    def __init__(self, filename) -> None:
        self.filename = filename
        self.load()

    def load(self):
        print(f"Loading ebook {self.filename}")

    def show(self):
        print(f"Showing ebook {self.filename}")

    def get_filename(self):
        return self.filename
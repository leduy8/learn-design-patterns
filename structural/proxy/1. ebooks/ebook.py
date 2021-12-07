from abc import ABC, abstractmethod


class Ebook(ABC):
    @abstractmethod
    def show(self):
        pass

    def get_filename(self):
        pass
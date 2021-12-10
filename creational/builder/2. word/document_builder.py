from abc import ABC, abstractmethod


class DocumentBuilder(ABC):
    @abstractmethod
    def add(self, element):
        pass
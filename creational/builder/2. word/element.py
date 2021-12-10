from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def get_content(self):
        pass
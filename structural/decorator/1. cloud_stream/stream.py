from abc import ABC, abstractmethod


class Stream(ABC):
    @abstractmethod
    def write(self, data):
        pass
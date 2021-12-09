from abc import ABC, abstractmethod


class Calendar(ABC):
    @abstractmethod
    def add_event(self, event, date):
        pass
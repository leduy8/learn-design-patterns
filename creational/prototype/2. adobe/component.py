from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def clone(self):
        pass
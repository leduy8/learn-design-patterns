from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def action_when_fire_occure(self):
        pass
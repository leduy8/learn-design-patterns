from abc import ABC, abstractmethod

class DialogBox(ABC):
    @abstractmethod
    def changed(control):
        pass
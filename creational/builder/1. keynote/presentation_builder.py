from abc import ABC, abstractmethod


class PresentationBuilder(ABC):
    @abstractmethod
    def add_slide(self, slide):
        pass
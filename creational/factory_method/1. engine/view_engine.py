from abc import ABC, abstractmethod


class ViewEngine(ABC):
    @abstractmethod
    def render(self, viewname, context):
        pass
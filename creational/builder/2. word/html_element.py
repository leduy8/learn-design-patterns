from abc import ABC, abstractmethod


class HtmlElement(ABC):
    @abstractmethod
    def get_content(self):
        pass
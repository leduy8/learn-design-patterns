from abc import ABC, abstractmethod


class EmailProvider(ABC):
    @abstractmethod
    def download_email(self, email):
        pass
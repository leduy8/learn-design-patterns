from abc import ABC, abstractmethod


class Plan(ABC):
    @abstractmethod
    def plan_details(self):
        pass
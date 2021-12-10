from abc import ABC, abstractmethod


class PlanFactory(ABC):
    @abstractmethod
    def create_meal_plan(self):
        pass

    @abstractmethod
    def create_workout_plan(self):
        pass
from plan_factory import PlanFactory
from weight_loss_workout_plan import WeightLossWorkoutPlan
from weight_loss_meal_plan import WeightLossMealPlan


class WeightLossPlanFactory(PlanFactory):
    def create_meal_plan(self):
        return WeightLossMealPlan()

    def create_workout_plan(self):
        return WeightLossWorkoutPlan()
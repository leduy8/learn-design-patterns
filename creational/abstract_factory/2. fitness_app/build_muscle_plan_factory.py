from plan_factory import PlanFactory
from build_muscle_meal_plan import BuildMuscleMealPlan
from build_muscle_workout_plan import BuildMuscleWorkoutPlan


class BuildMusclePlanFactory(PlanFactory):
    def create_meal_plan(self):
        return BuildMuscleMealPlan()

    def create_workout_plan(self):
        return BuildMuscleWorkoutPlan()
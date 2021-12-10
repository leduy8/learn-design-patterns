class HomePage:
    def set_goal(self, factory):
        factory.create_meal_plan(self).plan_details()
        factory.create_workout_plan(self).plan_details()
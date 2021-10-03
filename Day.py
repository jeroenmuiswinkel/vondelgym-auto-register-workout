from typing import List

from Workout import Workout


class Day:
    def __init__(self, selenium_day_object):
        self.selenium_day_object = selenium_day_object

    @property
    def workouts(self) -> List[Workout]:
        selenium_workout_objects = self.selenium_day_object.find_elements_by_class_name(
            "res_activities"
        )
        return [Workout(workout) for workout in selenium_workout_objects]

    @property
    def day(self) -> str:
        return self.selenium_day_object.find_element_by_class_name("date_day").text

    @property
    def date(self) -> str:
        return self.selenium_day_object.find_element_by_class_name("date_dd").text

    def __str__(self) -> str:
        workout_titles = [workout.__str__() for workout in self.workouts]
        return f"Classes on {self.day} {self.date}: \n" + "\n".join(workout_titles)

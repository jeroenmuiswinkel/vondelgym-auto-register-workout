class Workout:
    def __init__(self, workout_selenium_object):
        self.workout_selenium_object = workout_selenium_object

    @property
    def time(self):
        return self.workout_selenium_object.find_element_by_class_name("sp_time").get_attribute(
            "innerHTML"
        )

    @property
    def title(self):
        return self.workout_selenium_object.find_element_by_class_name("sp_title").get_attribute(
            "innerHTML"
        )

    @property
    def staff(self):
        return self.workout_selenium_object.find_element_by_class_name("sp_staff").get_attribute(
            "innerHTML"
        )

    def __str__(self):
        return f"{self.title} at {self.time} given by {self.staff}."

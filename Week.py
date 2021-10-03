from Day import Day


class Week:
    def __init__(self, selenium_day_objects):
        self.selenium_day_objects = selenium_day_objects

    @property
    def days(self):
        return [Day(day) for day in self.selenium_day_objects]

    def __str__(self):
        day_summaries = [day.__str__() for day in self.days]
        return "WEEK SUMMARY: \n" + "\n\n".join(day_summaries)

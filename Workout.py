import time

from driver import driver


class Workout:
    def __init__(self, workout_selenium_object):
        self.workout_selenium_object = workout_selenium_object

    @property
    def time(self) -> str:
        return self.workout_selenium_object.find_element_by_class_name("sp_time").get_attribute(
            "innerHTML"
        )

    @property
    def title(self) -> str:
        return self.workout_selenium_object.find_element_by_class_name("sp_title").get_attribute(
            "innerHTML"
        )

    @property
    def staff(self) -> str:
        return self.workout_selenium_object.find_element_by_class_name("sp_staff").get_attribute(
            "innerHTML"
        )

    @property
    def availability(self) -> str:
        return self.workout_selenium_object.find_element_by_class_name("available").get_attribute(
            "innerHTML"
        )

    @property
    def people_enlisted(self) -> int:
        return int(self.availability.split(" / ")[0])

    @property
    def workout_spots(self) -> int:
        return int(self.availability.split(" / ")[1])

    @property
    def full(self) -> bool:
        return self.people_enlisted == self.workout_spots

    def reserve(self) -> None:
        if not self.full:
            reserve_button = self.workout_selenium_object.find_element_by_class_name("reserve")
            reserve_button.click()
            time.sleep(1)
            alert = driver.switch_to.alert
            print(f"Vondelgym says: {alert.text}")
            alert.accept()
        else:
            print("class is already full")

    def cancel(self) -> None:
        cancel_button = self.workout_selenium_object.find_element_by_class_name("cancel")
        cancel_button.click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        alert = driver.switch_to.alert
        print(f"Vondelgym says: {alert.text}")
        alert.accept()

    def __str__(self) -> str:
        return f"{self.title} ({self.people_enlisted}/{self.workout_spots}) at {self.time} given by {self.staff}."

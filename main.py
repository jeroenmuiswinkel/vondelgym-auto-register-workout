import os

from dotenv import load_dotenv

from driver import driver
from Week import Week

load_dotenv()

USER_NAME = os.getenv("username")
PASSWORD = os.getenv("password")


driver.get("https://vondelgym.nl/")

login_button = driver.find_element_by_class_name("login_button")
login_button.click()

username_input = driver.find_element_by_id("f_email_").send_keys(USER_NAME)
password_input = driver.find_element_by_id("f_password_").send_keys(PASSWORD)
submit = driver.find_element_by_id("submit_button_2377").click()

driver.get("https://vondelgym.nl/lesrooster-vondelgym-zuid")


nb_days = len(driver.find_elements_by_class_name("res_days"))

week = Week([driver.find_element_by_id(f"res_day_{i+1}") for i in range(nb_days)])


print(f"Page Title is : {driver.title} \n")
print()
print("days available: ")
for i, day in enumerate(week.days):
    print(f"{i} {day.day} {day.date}")
print()
print("workouts on day 5:")
for i, workout in enumerate(week.days[4].workouts):
    print(f"{i} {workout}")

driver.find_element_by_id("button_add_to_home_no").click()

driver.find_element_by_id("res_day_5").click()
week.days[4].workouts[0].reserve()
print()
week.days[4].workouts[0].cancel()

# print([f"{day.day} {day.date}" for day in week.days])
# print()
# print("overview of lessons in the next week:")
# print(week)
driver.close()

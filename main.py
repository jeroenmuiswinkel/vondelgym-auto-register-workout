import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Day import Day
from Week import Week

load_dotenv()

USER_NAME = os.getenv("username")
PASSWORD = os.getenv("password")

options = Options()
options.headless = False

driver = webdriver.Chrome(options=options)
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
print(week)
driver.close()

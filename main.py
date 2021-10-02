from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://vondelgym.nl/")
element = driver.find_elements_by_class_name("login_button")
element.click()
print("Page Title is : %s" % driver.title)
# driver.quit()

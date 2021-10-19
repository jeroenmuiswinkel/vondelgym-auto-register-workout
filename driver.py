from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False

driver = webdriver.Chrome(options=options)

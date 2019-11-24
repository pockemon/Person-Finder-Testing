from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

size = driver.get_window_size()
print(size)
driver.execute_script("document.body.style.zoom='400%'")

size = driver.get_window_size()
print(size)

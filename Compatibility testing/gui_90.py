from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

size = driver.get_window_size()
print(size)
driver.execute_script("document.body.style.zoom='400%'")

size = driver.get_window_size()
print(size)

#This test has to be done manually and cannot be automated

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Ie(executable_path="D:\python programs\Driver for selenium\iedriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

size = driver.get_window_size()
print(size)
driver.execute_script("document.body.style.zoom='400%'")

button = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div")

align = selenium.getAttribute("button@align");

size = driver.get_window_size()
print(size)

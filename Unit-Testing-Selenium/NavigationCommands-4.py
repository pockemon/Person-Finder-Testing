from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

time.sleep(5)

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)

driver.get("http://pockemon.github.io/")

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.close()




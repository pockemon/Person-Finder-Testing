from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

print(driver.title)

print(driver.current_url)

driver.close()




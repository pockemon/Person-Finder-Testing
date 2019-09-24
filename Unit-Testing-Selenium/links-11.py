from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")

#(By.TAG_NAME, "a")

print(len(links))

driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "CON").click()

driver.close()

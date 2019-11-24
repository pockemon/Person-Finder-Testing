from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

element = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/a")

driver.execute_script("arguments[0].scrollIntoView();",element)

time.sleep(2)

driver.get("https://google.org/personfinder/test/results?role=seek&query_name=Ram+Sharma")

time.sleep(1)

element = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/a")

driver.execute_script("arguments[0].scrollIntoView();",element)

time.sleep(2)

driver.get("https://google.org/personfinder/test/view?family_name=&given_name=&id=test.personfinder.google.org%2Fperson.6322611528269824&query_location=&query_name=Ram+Sharma&role=seek")

time.sleep(1)

element = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/a")

driver.execute_script("arguments[0].scrollIntoView();",element)

time.sleep(2)

driver.close()

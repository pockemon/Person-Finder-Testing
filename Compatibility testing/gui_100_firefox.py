##This test case is failing because of the security feature of reCaptcha which prevents any automation tool or script from clicking on it.
#However the manual testing reveals that a confirmation message gets displayed on succesfully updating any field

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[2]/div/a").click()
time.sleep(10)

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/span[2]/input").send_keys("Shah")

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[3]/span[2]/input").send_keys("Raman")

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[5]/input").click()

time.sleep(10)

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[2]/div[1]/div[3]/a/span").click()

time.sleep(10)

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div[1]/div[2]/form/div/input").click()

time.sleep(10)

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/div[2]/textarea").send_keys("I met this person at MG Road on 5th November")

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/span[2]/input").send_keys("Raja")

driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div[1]/form/div/div[1]/div[1]/div[4]/input").click()

time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div/form/input").send_keys("h@gmail.com")
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div/form/div[3]/div[1]/input").click()
time.sleep(1)

if(driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/text()")):
	print("Success")
else:
	print("Failure")

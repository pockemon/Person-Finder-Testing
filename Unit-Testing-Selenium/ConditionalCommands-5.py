from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

usr_name = driver.find_element_by_name("userName")
print(usr_name.is_displayed())
print(usr_name.is_enabled())

pwd = driver.find_element_by_name("password")
print(pwd.is_displayed())
print(pwd.is_enabled())

usr_name.send_keys("hmr_270")
pwd.send_keys("1234567")

driver.find_element_by_name("login").click()

roundtrip_radio_status = driver.find_element_by_css_selector("input[value=roundtrip]")

print(roundtrip_radio_status.is_selected()) #print status of roundtrip btn

oneway_radio_status = driver.find_element_by_css_selector("input[value=oneway]")

print(oneway_radio_status.is_selected())

driver.close()
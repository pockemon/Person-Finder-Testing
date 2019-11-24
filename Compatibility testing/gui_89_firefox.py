from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

size_button = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a").value_of_css_property("font-size")
size_disclaimer = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]").value_of_css_property("font-size")

size_button = int(int(size_button[0])+int(size_button[1]))
size_disclaimer = int(int(size_disclaimer[0])+int(size_disclaimer[1]))

#print(type(size_button))
#print(type(size_disclaimer))

if(size_button<11 or size_disclaimer<11):
        print("Fail")
else:
        print("Pass")

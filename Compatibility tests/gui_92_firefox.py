from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
import time
import re
import ast

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)

color_btn_rgb = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]").value_of_css_property("background-color")
#the following steps are performed to convert the color coding from rgb format to hex format
r, g, b, alpha = ast.literal_eval(color_btn_rgb.strip("rgba"))
color_btn = '#%02x%02x%02x' % (r, g, b)
#print (hex_value)

color_disclaimer_rgb = driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]").value_of_css_property("color")
r, g, b, alpha = ast.literal_eval(color_disclaimer_rgb.strip("rgba"))
color_disclaimer = '#%02x%02x%02x' % (r, g, b)
#print(color_disclaimer)


if(color_btn == '#4285f4' and color_disclaimer == '#666666'):
	print("Success")
else:
	print("Failure")

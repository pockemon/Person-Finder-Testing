from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ast

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test/create?query=&given_name=ram&family_name=sharma&role=provide")
time.sleep(1)

submit_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div/div[5]/input").click()
time.sleep(1)

error_color_rgb = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div/div[7]").value_of_css_property("color")

#the following steps are performed to convert the color coding from rgb format to hex format
r, g, b = ast.literal_eval(error_color_rgb.strip("rgb"))
error_color = '#%02x%02x%02x' % (r, g, b)

#print(error_color)
if(error_color == '#ff0000'):
	print("success")
else:
	print("Failure")

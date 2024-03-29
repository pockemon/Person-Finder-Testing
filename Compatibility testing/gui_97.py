from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ast

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("https://google.org/personfinder/test/view?family_name=&given_name=&id=test.personfinder.google.org%2Fperson.6322611528269824&query_location=&query_name=Ram+Sharma&role=seek")
time.sleep(1)

link_color_rgb = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/a").value_of_css_property("color")

#the following steps are performed to convert the color coding from rgb format to hex format
r, g, b, alpha = ast.literal_eval(link_color_rgb.strip("rgba"))
link_color = '#%02x%02x%02x' % (r, g, b)

spam_link_color_rgb = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[2]/div[2]/span/a").value_of_css_property("color")

#print(spam_link_color_rgb)

#the following steps are performed to convert the color coding from rgb format to hex format
r, g, b, alpha = ast.literal_eval(spam_link_color_rgb.strip("rgba"))
spam_link_color = '#%02x%02x%02x' % (r, g, b)

#print(error_color)
if(spam_link_color == '#ff0000' and link_color == '#4285f4'):
	print("Success")
else:
	print("Failure")

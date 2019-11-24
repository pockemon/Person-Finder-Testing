from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test/results?role=seek")
time.sleep(1)
name_box = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/input").send_keys("Unknown")
driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/input").send_keys(Keys.ENTER)
time.sleep(1)
error_msg = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/h1")
if(error_msg):
    print("Test sucess")
else:
    print("Test fail")

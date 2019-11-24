from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Ie(executable_path="D:\python programs\Driver for selenium\iedriver.exe")

driver.get("https://google.org/personfinder/test")
time.sleep(1)
blue_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div")
blue_btn.click()
time.sleep(5)

name_box = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/input").send_keys("Unknown")
driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/input").send_keys(Keys.ENTER)
time.sleep(5)

new_user_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/form").click()
time.sleep(5)

fam_name = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div/div[2]/div[1]/span[2]/input").send_keys("Sharma")
first_name = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div/div[2]/div[2]/span[2]/input").send_keys("Ram")
create_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div/div[4]/input").click()
time.sleep(5)

skip_btn = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div/form/div[3]/div[2]/input").click()
time.sleep(5)

if driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div[1]/div[1]/div/div[1]/h1"):
    print("Success")
else:
    print("Fail")




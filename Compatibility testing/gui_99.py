from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("https://google.org/personfinder/test/view?family_name=&given_name=&id=test.personfinder.google.org%2Fperson.5595418535788544&query_location=&query_name=Raman+Shah&role=seek")
time.sleep(1)

element = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span/a/img")

size1 = (element.size)

#element = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[2]")

#size2 = (element.size)

print(size1)
#print(size2)

#############if the width and height of the element is less than 250px then the test is success

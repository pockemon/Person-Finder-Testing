from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#options = webdriver.ChromeOptions()
#options.binary_location = "D:/python programs/Driver for selenium/operadriver.exe"
#driver = webdriver.Opera(opera_options=options)

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")
driver.get("https://google.org/personfinder/test")
time.sleep(1)
blue_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div")
green_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[2]/div")

print("Size of blue button is: ",blue_btn.size)
print("Size of green button is: ",green_btn.size)

if blue_btn.size == green_btn.size:
    print("Test success")
else:
    print("Test fail")

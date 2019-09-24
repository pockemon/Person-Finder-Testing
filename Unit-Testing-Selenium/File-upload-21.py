from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame("frame-one1434677811")

time.sleep(3)
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("E://Internship documents/IEM-Cetificate.png")

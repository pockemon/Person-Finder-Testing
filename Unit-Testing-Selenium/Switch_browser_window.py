from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

time.sleep(3)

handler = driver.window_handles

for handle in handler:
    driver.switch_to_window(handle)
    print(driver.title)

driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\python programs\Driver for selenium\chromedriver.exe")

driver.get("http://w3schools.com/html/html_tables.asp")

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th"))

print(rows)
print(cols)

print("Company                                   Contact                     Country")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='                ')
    print()

driver.close()
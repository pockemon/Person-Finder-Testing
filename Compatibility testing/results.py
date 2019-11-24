Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_88_ie.py ==========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_88_ie.py", line 14, in <module>
    name_box = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/input").send_keys("Unknown")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to find element with xpath == /html/body/div/div[4]/div[1]/div/form/div/div[2]/input

>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_88_ie.py ==========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_88_ie.py", line 14, in <module>
    name_box = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/input").send_keys("Unknown")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to find element with xpath == /html/body/div/div[4]/div[1]/div/form/div/div[2]/input

>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_88_ie.py ==========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_88_ie.py", line 14, in <module>
    name_box = driver.find_element_by_xpath("//*[@id='query_name']").send_keys("Unknown")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to find element with xpath == //*[@id='query_name']

>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_88_firefox.py =======
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_88_firefox.py", line 14, in <module>
    name_box = driver.find_element_by_xpath("//*[@id='query_name']/div[1]/div/form/div/div[2]/input").send_keys("Unknown")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: //*[@id='query_name']/div[1]/div/form/div/div[2]/input

>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
Traceback (most recent call last):
  File "D:\python programs\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "D:\python programs\lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "D:\python programs\lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] The system cannot find the file specified

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 5, in <module>
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
  File "D:\python programs\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 73, in __init__
    self.service.start()
  File "D:\python programs\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
20px
13px
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 16, in <module>
    if(size_button<11 or size_disclaimer<11):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
20px
13px
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 16, in <module>
    if(int(size_button)<11 or int(size_disclaimer)<11):
ValueError: invalid literal for int() with base 10: '20px'
>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
<class 'str'>
<class 'str'>
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 16, in <module>
    if(size_button<11 or size_disclaimer<11):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
<class 'str'>
<class 'str'>
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 16, in <module>
    size_button = int(size_button)
ValueError: invalid literal for int() with base 10: '20px'
>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 10, in <module>
    size_button = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a").value_of_css_property("font-size")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a"}
  (Session info: chrome=78.0.3904.108)

>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 10, in <module>
    size_button = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a").value_of_css_property("font-size")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a"}
  (Session info: chrome=78.0.3904.108)

>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 10, in <module>
    size_button = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a").value_of_css_property("font-size")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div/div[4]/div[1]/div/div/div[1]/div[1]/div/a"}
  (Session info: chrome=78.0.3904.108)

>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
<class 'str'>
<class 'str'>
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 19, in <module>
    if(size_button<11 or size_disclaimer<11):
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\GUI testing\gui_89.py", line 7, in <module>
    driver.get("https://google.org/personfinder/test")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 333, in get
    self.execute(Command.GET, {'url': url})
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message: timeout
  (Session info: chrome=78.0.3904.108)

>>> 
===== RESTART: D:\python programs\SeleniumProject\GUI testing\gui_89.py =====
<class 'str'>
<class 'str'>
<class 'int'>
<class 'int'>
Fail
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_89_ie.py ==========
Fail
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_89_firefox.py =======
Fail
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_90.py ===========
{'width': 1051, 'height': 806}
{'width': 1051, 'height': 806}
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_90_firefox.py =======
{'width': 1294, 'height': 779}
{'width': 1294, 'height': 779}
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_90_ie.py ==========
{'width': 960, 'height': 614}
{'width': 960, 'height': 614}
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_91.py ===========
{'width': 1051, 'height': 806}
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_91.py", line 18, in <module>
    align = selenium.getAttribute("button@align");
NameError: name 'selenium' is not defined
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_92.py ===========
Success
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_92_firefox.py =======
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_92_firefox.py", line 15, in <module>
    r, g, b, alpha = ast.literal_eval(color_btn_rgb.strip("rgba"))
ValueError: not enough values to unpack (expected 4, got 3)
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_92_ie.py ==========
Success
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_93.py ===========
Traceback (most recent call last):
  File "D:\python programs\lib\site-packages\selenium\webdriver\common\service.py", line 76, in start
    stdin=PIPE)
  File "D:\python programs\lib\subprocess.py", line 709, in __init__
    restore_signals, start_new_session)
  File "D:\python programs\lib\subprocess.py", line 997, in _execute_child
    startupinfo)
FileNotFoundError: [WinError 2] The system cannot find the file specified

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_93.py", line 6, in <module>
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
  File "D:\python programs\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 73, in __init__
    self.service.start()
  File "D:\python programs\lib\site-packages\selenium\webdriver\common\service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home

>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_93.py ===========
success
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_93_firefox.py =======
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_93_firefox.py", line 17, in <module>
    r, g, b, alpha = ast.literal_eval(error_color_rgb.strip("rgba"))
ValueError: not enough values to unpack (expected 4, got 3)
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_93_ie.py ==========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_93_ie.py", line 11, in <module>
    submit_btn = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div/div[5]/input").click()
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.MoveTargetOutOfBoundsException: Message: Cannot click on element

>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_94.py ===========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_94.py", line 29, in <module>
    urllib.urlretrieve(image, 'remote.png')
AttributeError: module 'urllib' has no attribute 'urlretrieve'
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_94.py ===========
4adb6355958cbb2455697645d99dadfa
d40cf3c715d0ba219ad057c8c2546a33
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_94_firefox.py =======
4adb6355958cbb2455697645d99dadfa
d40cf3c715d0ba219ad057c8c2546a33
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_94_ie.py ==========
4adb6355958cbb2455697645d99dadfa
d40cf3c715d0ba219ad057c8c2546a33
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_96.py ===========
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_96.py ===========
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_96_firefox.py =======
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_96_ie.py ==========
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_97.py ===========
Success
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_97_firefox.py =======
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_97_firefox.py", line 14, in <module>
    r, g, b, alpha = ast.literal_eval(link_color_rgb.strip("rgba"))
ValueError: not enough values to unpack (expected 4, got 3)
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_97_ie.py ==========
Success
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_99.py ===========
{'height': 186, 'width': 250}
>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_99_firefox.py =======
{'height': 186.34999084472656, 'width': 250.0}
>>> 
========== RESTART: D:\python programs\SeleniumProject\gui_99_ie.py ==========
{'height': 186, 'width': 250}
>>> 
=========== RESTART: D:\python programs\SeleniumProject\gui_100.py ===========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_100.py", line 43, in <module>
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]"}
  (Session info: chrome=78.0.3904.108)

>>> 
======= RESTART: D:\python programs\SeleniumProject\gui_100_firefox.py =======
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_100_firefox.py", line 40, in <module>
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div/div/form/input").send_keys("h@gmail.com")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: /html/body/div[1]/div[4]/div[1]/div/div/form/input

>>> 
========= RESTART: D:\python programs\SeleniumProject\gui_100_ie.py =========
Traceback (most recent call last):
  File "D:\python programs\SeleniumProject\gui_100_ie.py", line 16, in <module>
    driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/form/div/div[2]/span[2]/input").send_keys("Shah")
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\python programs\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to find element with xpath == /html/body/div/div[4]/div[1]/div/form/div/div[2]/span[2]/input

>>> 

#the test case says that we are testing for clarity of image. But as we couldnt figure out how to do that, we instead tested for the situation
#that the image uploaded is the correct one or not. i.e is the image which is uploaded the actual one which we uploaded or did it get stored in an improper manner in the database such that the image which is shown on the screen is not the image which was actually uploaded

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import hashlib

def hash_it(path):
    with open(path, 'rb') as f:
        hasher = hashlib.md5()
        hasher.update(f.read())
        return hasher.hexdigest()

#directory = "C:home/har/Software Testing/GUI testing"
#remote_img = "{}/{}".format(directory, "remote.jpeg")
#local_img = "{}/{}".format(directory, "local.jpeg")

local_img = "local.png"

driver = webdriver.Firefox(executable_path="D:\python programs\Driver for selenium\geckodriver.exe")

driver.get("https://google.org/personfinder/test/view?id=test.personfinder.google.org%2Fperson.5595418535788544")
time.sleep(1)

image = driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span/a/img").get_attribute("src")

import urllib.request
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(image, 'remote.png')

local_img_hash = hash_it(local_img)
remote_img_hash = hash_it("remote.png")
print(local_img_hash)

print(remote_img_hash)

#this is a very binary process and even if a single pixel is different the hashes wont match
#as the dimensions of the downloaded image and the one which is already in the system are different, the hashes are not matching
#try to find if possible and if time permits, a process which is not so binary and rigid and can consider and understand the small differences which the two images may have


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = ""
pwd = ""

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")

print "Facebook" in driver.title

elem = driver.find_element_by_id("email")
elem.send_keys(user)

elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)

elem.send_keys(Keys.RETURN)

time.sleep(10)

driver.close()

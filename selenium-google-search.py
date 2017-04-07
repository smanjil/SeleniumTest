

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

search = "programming"

driver = webdriver.Chrome()
driver.get("http://www.google.com")

print "Google" in driver.title

elem = driver.find_element_by_id("lst-ib")
elem.send_keys(search)

elem.send_keys(Keys.RETURN)

time.sleep(10)

driver.close()

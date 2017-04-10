
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'root'
password = '127.0.0.1'

driver = webdriver.Chrome()

driver.get('http://192.168.1.1/login.asp')

# username
elem = driver.find_element_by_id('username')
elem.send_keys(username)

# password
elem = driver.find_element_by_id('password')
elem.send_keys(password)

# submit
elem.send_keys(Keys.ENTER)

# network status
elem = driver.find_element_by_id('div_wan')
print elem

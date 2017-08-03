
from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('http://www.snugzusa.com/product/akcp34sm/')

elem = browser.find_element_by_xpath("//div[@id='option-slider-0']") \
		.find_elements_by_xpath("//div[starts-with(@id, 'option-slide-0')]")

src_list = []

for item in elem:
    print item.get_attribute("id")
    if item.is_displayed() and item.is_enabled():
        item.click()
        time.sleep(3)
        src_url = browser.find_element_by_id("product-main-image")
        print src_url.get_attribute("src")
        src_list.append(src_url.get_attribute("src"))

print src_list

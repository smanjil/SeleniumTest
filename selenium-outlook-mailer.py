
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = ''
password = ''

driver = webdriver.Chrome()

driver.get("https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=0&client-request-id=6ab95657-930f-4eba-af9a-8d081309ab64&domain_hint=growbydata.com&nonce=636271567227778813.946ecdcc-7b38-4f29-8761-b5c201abc551&state=%2fowa%2f%3frealm%3dgrowbydata.com%26authRedirect%3dtrue#")

# print dir(driver)

print "Sign in to your account" in driver.title

# username field
elem = driver.find_element_by_id("cred_userid_inputtext")
elem.send_keys(email)

# password field
elem = driver.find_element_by_id("cred_password_inputtext")
elem.send_keys(password)

time.sleep(2)
elem.send_keys(Keys.ENTER)

# cred_sign_in_button
# driver.find_element_by_xpath('//button[@id="cred_sign_in_button"]').click()

# new mail button
time.sleep(2)
driver.find_element_by_xpath('//button[@class="_fce_h _fce_f ms-fwt-r ms-fcl-np o365button"]').click()

# to input
time.sleep(10)
elem = driver.find_element_by_xpath('//div[@class="_fp_F"]/form/input')
elem.send_keys('pchettri@growbydata.com')
elem.send_keys(Keys.TAB)

# cc input
# time.sleep(10)
# elem = driver.find_element_by_xpath('//div[@class="_fp_F"]/form/input')
# elem.send_keys('abc@gmail.com')
# elem.send_keys(Keys.TAB)

# subject
time.sleep(5)
elem = driver.find_element_by_xpath('//div[@class="_mcp_02"]/input')
elem.send_keys('BOD 09-April-2017')

# message
time.sleep(10)
elem = driver.find_element_by_xpath('//div[@class="allowTextSelection _mcp_V1 customScrollBar ms-bg-color-white ms-font-color-black owa-font-compose"]')
elem.send_keys('hello there!!!!')

# send button
driver.find_element_by_xpath('//button[@title="Send"]').click()

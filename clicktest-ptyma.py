
from __future__ import print_function
from selenium import webdriver
import time
import pandas as pd

# urls_df = pd.read_csv('SnugzUrlsforimages_201707211.csv')
urls_df = pd.read_csv('remaining-urls.csv')

inv = open('invalid.csv', 'w')

browser = webdriver.Firefox()

# http://www.snugzusa.com/product/ZCO10C

with open("outputs-remaining.tsv",'w') as outputs:
	for url in urls_df['urls']:
		print(url)

		browser.get(url)

		try:
			elem = browser.find_element_by_xpath("//div[@id='option-slider-0']") \
					.find_elements_by_xpath("//div[starts-with(@id, 'option-slide-0')]")

			src_list = []

			for item in elem:
			    if item.is_displayed() and item.is_enabled():
			        item.click()
			        time.sleep(3)
			        src_url = browser.find_element_by_id("product-main-image")
			        src_list.append(src_url.get_attribute("src"))

			# urls_df['invalid_url'] = ''
			# urls_df['src-img-url'] = src_list
			print ("%s\t%s" % (url, src_list), file=outputs)

	 	except:
			print ('Invalid: ', url)
			print("%s" %(url), file=inv)
			# urls_df['src-img-url'] = ''
			# urls_df['invalid_url'] = url
			# 	print('Error! no variations available..')

inv.close()


# urls_df.to_csv('new-res.csv', index=False)

#!/usr/bin/env python
import time
import string
import urllib
import urllib.request
import http.cookiejar
from random import randint, choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def readconf(mylist,filename):
	conf = open(filename,"rb")
	for lines in conf:
		item = lines.rstrip(b"\r\n").decode("utf-8")
		mylist.append(item)
	conf.close

def main():
	
	for i in range(10):
		firstnames = []
		readconf(firstnames,'firstnames.txt')
		conchar = ['.','_']
		surnames = []
		readconf(surnames,'surnames.txt')
		doms = []
		readconf(doms,'doms.txt')
		email = choice(firstnames) + choice(conchar) + choice(surnames) + '@' + choice(doms)
		print(email)
		# if run hourly comment the following two lines out to make it more real.
		#waittime = randint(0,3600)
			#time.sleep(waittime)
		# myCookie = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
		# openner = urllib2.build_opener(myCookie)

		# specify the path to the webdriver for your preferred browser
		browser = webdriver.Chrome('/Users/juicef/Downloads/chromedriver_mac_arm64-2/chromedriver')

		# navigate to the webpage
		browser.get('https://forms.office.com/Pages/ResponsePage.aspx?id=FM9wg_MWFky4PHJAcWVDVuHLaopDgtdFgEbDRj_iBqxUOENQSkRLSUZUTUtVRlRGWVg1V0JHTzdXVS4u&fbclid=PAAaaG3cyxLbzCP_FXQmfBZfeKy1fy1ePyvmIbk6cLo2GeyFuMl_dJ5olL54Y')
		time.sleep(1)
		# find the text box element and enter text
		# text_box = browser.find_element(By.ID, 'textbox-id')
		# textbox = browser.find_element(By.XPATH, '//input[@value="Enter your answer"]')

		# input_element = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/div[3]/div/div/input")
		
		textbox = browser.find_element(By.XPATH, '//input[@placeholder="Enter your answer"]')

		textbox.send_keys(email)

		# select the radio button
		# radio_button = browser.find_element(By.ID, 'radio-button-id')
		radio_button = browser.find_element(By.XPATH, '//input[@value="ARENA"]')
		radio_button.click()


		# submit the form
		submit_button = browser.find_element(By.XPATH, "//div[text()='Submit']/ancestor::button")
		submit_button.click()
		time.sleep(1)

		# close the browser window
		browser.quit()

		# # this should be the <input name='vote[email]'> in the page
		# post_data = {'vote[email]':email,'vote[entry_id]':'115'}
		# #should match  <form method="post" id="voteform" name="vote" action="http://www.cenovis.com.au/win-the-goods-entry/index.php/enter/detail" >
		# req = urllib2.Request('http://www.cenovis.com.au/win-the-goods-entry/index.php/enter/detail', urllib.urlencode(post_data))
		# html_src = openner.open(req).read()
		result = open("voted.log","a")
		result.write(email+"\n")
		result.close()

if __name__ == "__main__":
    	main()






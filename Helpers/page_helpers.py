from helpers.mailgun import mail
from ui_tests_redis import UITestsRedis
import time

class PageHelpers(object):
	"""
		Check if page_source contains success code
	"""
	def __init__(self, browser):
		self.browser = browser
		self.driver = self.browser.get_web_driver()
		self.UITestsRedis = UITestsRedis()

	def get_screen_shot_path(self, url):
		return "/var/tmp/" + "_".join(url.split("/")[2:]) +time.strftime("%d_%m_%Y_%H_%M_%S") + ".png"

	def check_success_status(self, find_text):
		page_text = self.driver.page_source
		# Removing whitespace and lowering all html for comparision
		page_text = "".join([x.lower() for x in page_text.split()])
		find_text = "".join([x.lower() for x in find_text.split()])
		return True if page_text.find(find_text) >= 0 else False

	def get_screen_shot(self, url):
		# Save screen shot by removing https:// or http:// and replacing / with _
		path = self.get_screen_shot_path( url )
		self.browser.get_screen_shot( path )
		return path

	def check_for_result(self, url, success_string, result, screen_shot = True, update_redis = True):
		if self.check_success_status(success_string):
			if update_redis : self.UITestsRedis.update_result(url, time.time())
			# if screen_shot : self.get_screen_shot(url)
			result[url] = "passed"
			print result[url]
		else:
			if update_redis : self.UITestsRedis.update_result(url, 0)
			if screen_shot : path = self.get_screen_shot(url)
			result[url] = "failed"
			print result[url]
			mail("manav148@gmail.com", "UI Test Failed", time.strftime("%d/%m/%Y %H:%M:%S") +  " Results : " + str(result), path)

			
	def take_screen_shot_and_mail(self, url):
		path = self.get_screen_shot(url)
		mail("manav148@gmail.com", "UI Test Failed", time.strftime("%d/%m/%Y %H:%M:%S") +  " Results : " + str(url), path)

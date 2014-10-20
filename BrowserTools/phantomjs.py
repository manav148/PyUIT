from selenium import webdriver
import time
class PhantomJS(object):
	"""
	Starting PhantomJS and hooking with Selenium
	Instantiate:
	with PhantomJS() as phantomjs:
	"""

	def __init__(self, ssl= True, url = None):
		self.driver = webdriver.PhantomJS("phantomjs", service_args=['--ignore-ssl-errors=true']) if ssl else webdriver.PhantomJS('phantomjs')
		self.wait_after_getting_url = 60
		if url:
			self.url = url

	def get_screen_shot(self, file_path = "/var/tmp/ui_test_screenshot.png"):
		with file(file_path,'wb') as ui_screenshot:
			ui_screenshot.write(self.driver.get_screenshot_as_png())
		return file_path
	
	def get_url(self, url = None):
		if url:
			self.url = url
		self.driver.get(self.url)
		# time.sleep(self.wait_after_getting_url)

	def get_web_driver(self):
		return self.driver

	def purge_cookies(self):
		self.driver.delete_all_cookies()

	def get_page_source(self):
		return self.driver.page_source

	def __enter__(self):
		return self

	def __del__(self):
		self.driver.quit()

	def __exit__(self, type, value, traceback):
		self.driver.quit()


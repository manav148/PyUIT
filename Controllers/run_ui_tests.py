from BrowserTools import  FillForm, PhantomJS, Firefox
from Helpers import PageHelpers

class RunUITests(object):
	"""Parse Rules and Runs UI Tests"""
	def __init__(self, rules = None):
		self.rules = rules
		self.result = dict()
		# self.UITestsRedis = UITestsRedis()
		self.browser_name = None
		
	def set_rules(self, rules):
		self.rules = rules

	def run_ui_tests(self, browser_name = "phantomjs"):
		# Based on browser run corresponding UI tests
		self.browser_name = browser_name
		if browser_name == "phantomjs":
			# neccesary if we have to access sites with https://
			with PhantomJS(ssl=True) as phantomjs:
				self.run_ui_tests_with_browser(phantomjs)
		elif browser_name == "firefox":
			with Firefox() as firefox:
				self.run_ui_tests_with_browser(firefox)

	def run_ui_tests_with_browser(self, browser):
		# get driver from browser
		driver = browser.get_web_driver()
		# initiate page helpers class
		page_helpers = PageHelpers(browser)
		# Parse rules and run tests
		for rule in self.rules:
			try:
				# Write tests using fillform class to submit forms (common)
				# or visit links
				pass
			except Exception, e:
				# Take screen shot and email in case of failure
				page_helpers.take_screen_shot_and_mail()
				raise e
			# Purging cookies to start a new test
			browser.purge_cookies()

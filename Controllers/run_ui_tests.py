from BrowserTools import  FillForm, PhantomJS, Firefox
from Helpers import PageHelpers, ImportContacts, ImportContactsNew

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
			with PhantomJS(ssl=True) as phantomjs:
				self.run_ui_tests_with_browser(phantomjs)
		elif browser_name == "firefox":
			with Firefox() as firefox:
				self.run_ui_tests_with_browser(firefox)

	def run_ui_tests_with_browser(self, browser):
		# Parse rules and run tests
		for rule in self.rules:
			# print "Rule : ", str(rule)
			for page in rule:
				try:
					print page
					# If the url contains import initialize import module
					if page['url'].find("import?p") >= 0:
						import_contacts = ImportContactsNew(rules = page, browser = browser, result = self.result)
						import_contacts.start_importing_contacts()
					# proceed normal requests
					else:
						browser.get_url(page['url'])
						driver = browser.get_web_driver()
						# browser.get_page_source()
						page_helpers = PageHelpers(browser)
						# For each form fill one form
						fillform = FillForm(driver)
						if page['fields']:
							for field, value in page['fields'].iteritems():
								fillform.set_element_by_name(field, value)
							fillform.submit_form()
						# Check if the page contains the desired text
						screen_shot = True if self.browser_name == "phantomjs" else False
						page_helpers.check_for_result( url = page['url'], success_string = page['success'], result = self.result, screen_shot = screen_shot, update_redis = True)
				except Exception, e:
					if page_helpers:
						page_helpers.take_screen_shot_and_mail(page['url'])
					raise e
			# Purging cookies to start a new test
			print "\nPurging cookies\n"
			browser.purge_cookies()
		print "\nResult : \n"+ str(self.result)

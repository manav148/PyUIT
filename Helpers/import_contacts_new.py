import time
from BrowserTools import  FillForm
from page_helpers import PageHelpers

class ImportContactsNew(object):
	"""
		Import contacts from user account
	"""
	def __init__(self, rules, browser, result):
		self.rules = rules
		self.browser = browser
		# result dict of run ui tests to which we append the results
		self.result = result
		self.page_helpers = PageHelpers(browser)
		self.sleep_before_inviting = 120
		self.gmail_windows_opened = set()
		self.myz_handle = False
		self.other_window = False

	def check_gmail_window(self, title):
		return True if (title.lower().find("gmail") >= 0 or title.lower().find("google") >= 0) else False

	def switch_to_gmail_window(self):
		driver = self.browser.get_web_driver()
		# switch to gmail authentication window
		handles = driver.window_handles
		other_window = [handle for handle in handles if (handle != self.myz_handle and not set(handle).intersection(self.gmail_windows_opened)) ]
		if other_window:
			self.other_window = other_window[0]
			self.gmail_windows_opened.add(self.other_window)
			# if current window is not already changed
			if self.check_window_title() and driver.current_window_handle != self.other_window:
				print "Switching to handle : ", other_window
				driver.switch_to_window(self.other_window)
	
	def switch_to_myz_window(self):
		driver = self.browser.get_web_driver()
		# Switch back to myZ
		driver.switch_to_window(self.myz_handle)

	def check_window_title(self):
		driver = self.browser.get_web_driver()
		try:
			return driver.title
		except Exception:
			return False

	def check_if_already_authenticated(self):
		# Check if we have the authentication token we skip the rest
		driver = self.browser.get_web_driver()
		try:
			driver.find_elements_by_tag_name("button")
		except Exception:
			# didn't find any button it means user is already authenticated 
			return True
		return False
	

	def go_through_gmail_authentication(self):
		driver = self.browser.get_web_driver()
		fillform = FillForm(driver)
		fillform.click_visible_button_on_page()
		self.switch_to_gmail_window()
		if self.other_window and self.check_window_title():
			try:
				# Fill email and password
				fillform.set_text_element_by_id("Email", "picbumimporter@gmail.com")
				fillform.set_text_element_by_id("Passwd", "QLm6BWGOQiyJ01YRgjkng/bwxk+4rk8bOw==")
				fillform.submit_form()
			except Exception:
				# If cannot find this on this window pass move on to the next test
				print "We don't need to add authentication credentials lets move ahead"
				pass
		
		if self.other_window and self.check_window_title():
			# Fill approval form
			fillform = FillForm(driver)
			# this should close the authentication window
			fillform.submit_form(submit_by_id ="submit_approve_access")
		
		self.switch_to_myz_window()

	def start_importing_contacts(self):
		import_url = self.rules['url']
		driver = self.browser.get_web_driver()
		try:
			# Go to import page
			self.browser.get_url(import_url)
			# Set myz handle
			self.myz_handle = driver.current_window_handle if not self.myz_handle else self.myz_handle

			# Check If the user is already authenticated?
			if not self.check_if_already_authenticated():
				self.go_through_gmail_authentication()
		except Exception, e:
			self.page_helpers.take_screen_shot_and_mail(import_url)
			raise e
		# click on import contacts button should be forwarded
		print driver.current_url
		# find if it is on import page
		on_import_page = True if self.browser.get_page_source().find(self.rules['success_on_import']) >= 0 else False
		if on_import_page:
			print "Already on import page"

		fillform = FillForm(driver)
		# If there is an error 
		error_elements = driver.find_elements_by_class_name("alert-error")
		if not error_elements and not on_import_page :
			print "No error and not on import page"
			fillform.click_visible_button_on_page()
		self.page_helpers.check_for_result(url = driver.current_url , success_string = self.rules['success_on_import'], result = self.result,
	 	screen_shot = True, update_redis = True)	
		
		fillform.click_visible_button_on_page()
		# time.sleep(self.sleep_before_inviting)		
		print driver.current_url
		self.page_helpers.check_for_result(url = driver.current_url , success_string = self.rules['final_success'], result = self.result,
		 	screen_shot = True, update_redis = True)		


import time

class Form(object):
	"""
	Submits form data into page 
	"""
	
	def __init__(self, driver):
		self.driver = driver
		self.wait_after_submission = 10 #seconds
		self.any_form_element = None
	
	def click_visible_button_on_page(self):
		buttons =  self.driver.find_elements_by_tag_name("button")
		for button in buttons:
			if button.is_displayed():
				button.click()
				# sleeping for specified time b4 moving forward
				time.sleep(self.wait_after_submission)
				break

	def get_wait_after_submission(self):
		return self.wait_after_submission

	def get_element_by_id(self, id):
		element = self.driver.find_element_by_id(id)
		self.set_any_form_element(element)
		return element

	def set_element_by_id(self, id, value):
		element = self.get_element_by_id(id)
		self.set_element_value(element, value)
		return element
	
	def set_any_form_element(self, element):
		# set for submitting the form 
		if (not self.any_form_element and element):
			self.any_form_element = element

	def set_first_element_by_name(self, name, value):
		element = self.get_first_element_by_name(name)
		self.set_element_value(element, value)
		return element

	def get_first_element_by_name(self, name):
		element = self.driver.find_elements_by_name(name)[0]
		self.set_any_form_element(element)
		return element

	def get_first_element_and_type_by_name(self, name):
		element = self.get_first_element_by_name(name)
		element_type = element.get_attribute("type")
		return dict(element = element, element_type = element_type)

	def get_elements_by_name(self, name):
		elements = self.driver.find_elements_by_name(name)
		self.set_any_form_element(elements[0])
		return elements

	def set_element_value(self, element, value):
		element.send_keys(value)
		self.set_any_form_element(element)

	def click_submit(self, any_form_element = None, submit_by_name = None, submit_by_id = None):
		# Preffered pass any for element and selenium will automatically submit it for us
		if any_form_element:
			any_form_element.submit()
		# Assumes there is only one submit button by name
		elif submit_by_name:
			self.get_first_element_by_name(submit_by_name).click()
		# Find submit button by id and click
		elif submit_by_id:
			self.get_element_by_id(submit_by_id).click()
		# if class has an intrinsic method use that
		elif self.any_form_element:
			self.any_form_element.submit()
		# Else lets assume the page has a submit button named submit which we will click
		else:
			self.get_first_element_by_name("submit").click()
		time.sleep(self.wait_after_submission)


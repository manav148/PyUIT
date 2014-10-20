from selenium.webdriver.support.ui import Select
from form import Form

class FillForm(Form):
	"""
		Wrapper for Form class
	"""
	def __init__(self, driver):
		super(FillForm, self).__init__(driver)
		self.form_filled = False

	def set_by_type(self, element, element_type, name, value):
		if element_type == "radio":
			self.set_radio_button_by_name(name, value)
		elif element_type == "submit":
			self.submit_form(submit_by_name = element_type)
			self.form_filled = True
		else:
			super(FillForm, self).set_element_value(element, value)

	def set_element_by_name(self, name, value):
		dict_element_type = super(FillForm, self).get_first_element_and_type_by_name(name)
		self.set_by_type(dict_element_type['element'], dict_element_type['element_type'], name, value)
	
	def set_radio_button_by_name(self, name, value):
		elements = super(FillForm, self).get_elements_by_name(name)
		for element in elements:
			form_value = str(element.get_attribute('value'))
			if str(value) == form_value:
				element.click()
				break

	def submit_form(self, any_form_element = None, submit_by_name = None, submit_by_id = None):
		if not self.form_filled:
			super(FillForm, self).click_submit(any_form_element, submit_by_name, submit_by_id)
			self.form_filled = True

	def get_radio_button_elements_by_id(self, id):
		# get element
		element = super(FillForm, self).get_element_by_id(id)
		# name of the radio group
		radio_group = element.get_attribute('name')
		# elements in the radio group
		return super(FillForm, self).get_elements_by_name(radio_group)

	def set_text_element_by_id(self, id,value):
		super(FillForm, self).set_element_by_id(id, value)
	
	def set_select_element_by_id(self, id, value):
		select = Select(super(FillForm, self).get_element_by_id(id))
		select.select_by_visible_text(value)
	
	def set_radio_button_by_id(self, id, value):
		elements = self.get_radio_button_elements_by_id(id)
		for element in elements:
			form_value = str(element.get_attribute('value'))
			if str(value) == form_value:
				element.click()
				break

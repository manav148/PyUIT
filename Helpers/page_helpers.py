class PageHelpers(object):
    """
        Add generic helpers used in UITests to this class
        Example: 
        -> Taking a screen shot and mailing if some test fails
        -> Writing data to database
        -> Check if test passed
    """
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.get_web_driver()

    def check_success_status(self, find_text):
        page_text = self.driver.page_source
        # Removing whitespace and lowering all html for comparision
        page_text = "".join([x.lower() for x in page_text.split()])
        find_text = "".join([x.lower() for x in find_text.split()])
        return True if page_text.find(find_text) >= 0 else False

    def get_screen_shot(self, url):
        pass

    def take_screen_shot_and_mail(self):
        pass

    def write_data_to_database(self, **argv):
        pass
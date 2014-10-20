class PageHelpers(object):
    """
        Add generic helpers used in UITests to this class
        Example: 
        -> Taking a screen shot and mailing if some test fails
        -> Writing data to database
    """
    def __init__(self, browser):
        self.browser = browser
        self.driver = self.browser.get_web_driver()

    def get_screen_shot(self, url):
        pass

    def take_screen_shot_and_mail(self, url):
        pass

    def write_data_to_database(self, **argv):
        pass
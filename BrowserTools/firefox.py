from selenium import webdriver

class Firefox(object):
    """
    Starting Firefox and hooking with Selenium
    Instantiate:
    with Firefox() as firefox:
        
    """
    def __init__(self, ssl= True, url = None):
        self.driver = webdriver.Firefox()
        if url:
            self.url = url

    def get_screen_shot(self, file_path = "./tmp.png"):
        with file(file_path,'wb') as ui_screenshot:
            ui_screenshot.write(self.driver.get_screenshot_as_png())
        return file_path
    
    def get_url(self, url = None):
        if url:
            self.url = url
        self.driver.get(self.url)

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


from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

import time
class Basepage(object):
    #打开网页
    def __init__(self,driver):
        self.driver =driver
    #

#保存图片
    def save_pic(self, locator):
        self.driver.get_screenshot_as_file(locator)




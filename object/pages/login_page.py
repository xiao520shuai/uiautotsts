from selenium.webdriver.support.wait import WebDriverWait
import time
from .base_page import Basepage
from .locators import LocatorLogin,first,last
class Login(Basepage):
    #点击弹出框
    def popclick(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*first.dismiss)
        )
        self.driver.find_element(*first.dismiss).click()
    #输入账号
    def input_email(self,data):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*LocatorLogin.email)
        )
        element = self.driver.find_element(*LocatorLogin.email)
        element.click()
        element.clear()
        element.send_keys(data)
    #输入密码
    def input_password(self, data):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*LocatorLogin.password)
        )
        element = self.driver.find_element(*LocatorLogin.password)
        element.click()
        element.clear()
        element.send_keys(data)
    #点击登陆
    def one_click(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*LocatorLogin.loginButton)
        )
        element = self.driver.find_element(*LocatorLogin.loginButton)
        element.click()
    #退出账号
    def quite_qiute(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*last.quit1)
        )
        self.driver.find_element(*last.quit1).click()
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*last.quit2)
        )
        self.driver.find_element(*last.quit2).click()

    #验证成功
    def assert_login_success(self):
        return self.driver.page_spurce
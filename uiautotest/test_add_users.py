from selenium import webdriver
import time
from unittest import TestCase
from ddt import ddt,data,unpack,file_data
from selenium.webdriver.support.select import Select


@ddt
class TestHrm(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"D:\project\uiautotest\chromedriver.exe")
        cls.driver.implicitly_wait(10)
    def test_1login(self):
        self.driver.get("http://114.116.97.187:8080/symfony/web/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("Bitnami.12345")
        self.driver.find_element_by_id("btnLogin").click()
    @data(['王 帅',"2345675",'!Ws921434152','!Ws921434152'],
          ['王 帅',"2345676",'!Ws921434152','!Ws921434152'])
    def test_2add_jobTitle(self,value):
        self.driver.get("http://114.116.97.187:8080/symfony/web/index.php/admin/saveSystemUser")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Select(self.driver.find_element_by_id("systemUser_userType")).select_by_visible_text("管理员")
        self.driver.find_element_by_name('systemUser[employeeName][empName]').send_keys(value[0])
        self.driver.find_element_by_name('systemUser[userName]').send_keys(value[1])
        self.driver.find_element_by_name('systemUser[password]').send_keys(value[2])
        self.driver.find_element_by_name('systemUser[confirmPassword]').send_keys(value[3])
        self.driver.find_element_by_id("btnSave").click()
        # time.sleep(1)
        # assert value[0] in self.driver.page_source
        # time.sleep(1)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
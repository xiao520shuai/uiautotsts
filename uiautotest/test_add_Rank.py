from selenium import webdriver
import time
from unittest import TestCase
from ddt import ddt,data,unpack,file_data
from uiautotest import readcsv
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
    # @data(['aa5',"回归测试",r'D:\project\uiautotest\1.png',"合作完成工作"],
    #       ['aa6',"回归测试",r'D:\project\uiautotest\1.png',"合作完成工作"])
    # @file_data(r'D:\project\uiautotest\juice_data2.yml')
    @data(readcsv.readcsv(r'D:\project\uiautotest\data.csv'))
    def test_2add_jobTitle(self,value):
        print(value)
        print(value[0])
        self.driver.get("http://114.116.97.187:8080/symfony/web/index.php/admin/viewJobTitleList")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.find_element_by_id("btnAdd").click()
        self.driver.find_element_by_name('jobTitle[jobTitle]').send_keys(value[0])
        self.driver.find_element_by_name('jobTitle[jobDescription]').send_keys(value[1])
        # self.driver.find_element_by_id('jobTitle_jobSpec').send_keys(value)
        self.driver.find_element_by_name('jobTitle[note]').send_keys(value[2])
        self.driver.find_element_by_name("btnSave").click()

        # time.sleep(1)
        # assert value[0] in self.driver.page_source
        # time.sleep(1)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path=r"D:\project\uiautotest\chromedriver.exe")
driver.get("http://114.116.97.187:8080/symfony/web/index.php/auth/login")
# driver.find_element_by_link_text("忘了密码?").click()
# time.sleep(2)
# driver.back()
# driver.find_element_by_id("txtUsername").send_keys("admin")
# driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("Bitnami.12345")
# driver.find_element_by_id("btnLogin").click()
time.sleep(2)
driver.close()
# driver.implicitly_wait(10)
# driver.maximize_window()  #最大化
# time.sleep(2)
# driver.get('https://cn.bing.com/')
# driver.back()  #回退
# time.sleep(2)
# driver.forward()   #页面刷新
# driver.get('http://114.116.97.187:8001')
# driver.refresh()   #截图
# driver.save_screenshot('1.png')
# driver.close()
# driver.find_element_by_id("txtUsername").send_keys("admin")
# driver.find_element_by_id("txtPassword").send_keys("Bitnami.12345")
# driver.find_element_by_id("btnLogin").click()
# assert 'Admin'in driver.page_source


from selenium import webdriver
from unittest import TestCase
import time
class TestHrm(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=r"/Users/lindafang/PycharmProjects/orange_it/uiautotest/chromedriver")
        cls.driver.implicitly_wait(10)

    def test_1login(self):
        self.driver.get("http://114.116.97.187:8080/symfony/web/index.php/auth/login")
        self.driver.find_element_by_id("txtUsername").send_keys("admin")
        self.driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("Bitnami.12345")
        self.driver.find_element_by_id("btnLogin").click()
    def test_2add_jobTitle(self):
        self.driver.get("http://114.116.97.187:8080/symfony/web/index.php/admin/viewJobTitleList")
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.find_element_by_id("btnAdd").click()
        self.driver.find_element_by_name("jobTitle[jobTitle]").send_keys("俄语教师2")
        self.driver.find_element_by_name("jobTitle[jobDescription]").send_keys("俄语")
        # self.driver.find_element_by_name("jobTitle[jobSpec]").send_keys("C:\\Users\Administrator\Desktop\杜玲辉-简历.pdf")
        self.driver.find_element_by_name("jobTitle[note]").send_keys("1111")
        self.driver.find_element_by_name("btnSave").click()
        assert "俄语教师1" in self.driver.page_source
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
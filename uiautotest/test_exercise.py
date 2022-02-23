from selenium import webdriver
import time
import pytest
import yaml
import allure
from selenium.webdriver.support.select import Select
@pytest.fixture(scope='session')
@allure.epic("管理员")
@allure.feature("登陆")
def driver():
    driver1 = webdriver.Chrome(executable_path=r"D:\project\uiautotest\chromedriver.exe")
    allure.attach("目标网址")
    driver1.get("http://114.116.97.187:8080/symfony/web/index.php/auth/login")
    allure.attach("输入账号")
    driver1.find_element_by_id("txtUsername").send_keys("admin")
    allure.attach("密码")
    driver1.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("Bitnami.12345")
    driver1.find_element_by_id("btnLogin").click()
    yield driver1
    driver1.quit()
@allure.epic("管理员")
@allure.feature("职称")
@allure.story("添加职称")
@allure.testcase("http://114.116.97.187:8086/zentao/")
@allure.issue("http://114.116.97.187:8086/zentao/bug", "职称名字重复")
@pytest.mark.parametrize('test',yaml.safe_load(open('test_data.yml')))
def test_2add_jobTitle(driver,test):
    allure.attach("目标网址")
    driver.get("http://114.116.97.187:8080/symfony/web/index.php/admin/viewJobTitleList")
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element_by_id("btnAdd").click()
    allure.attach("职称名")
    driver.find_element_by_name('jobTitle[jobTitle]').send_keys(test['title'])
    allure.attach("职称简介")
    driver.find_element_by_name('jobTitle[jobDescription]').send_keys(test['desc'])
    # self.driver.find_element_by_id('jobTitle_jobSpec').send_keys(value)
    allure.attach("注释")
    driver.find_element_by_name('jobTitle[note]').send_keys("合作完成工作")
    driver.find_element_by_name("btnSave").click()
    driver.save_screenshot("job1.png")
    allure.attach.file("job1.png",attachment_type=allure.attachment_type.PNG)
    # assert test['title'] in driver.page_source
    # time.sleep(1)
    # ['aa5', "回归测试", r'D:\project\uiautotest\1.png', "合作完成工作"]





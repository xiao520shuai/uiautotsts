from selenium import webdriver
import pytest
import yaml
import allure
@allure.epic("管理员")
@allure.feature("登陆")
@pytest.fixture(scope='session')
def driver():
    driver1 = webdriver.Chrome(executable_path=r"D:\project\uiautotest\chromedriver.exe")
    allure.attach("登陆网址")
    driver1.get("http://114.116.97.187:8080/symfony/web/index.php/auth/login")
    driver1.find_element_by_id("txtUsername").send_keys("admin")
    driver1.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("Bitnami.12345")
    driver1.find_element_by_id("btnLogin").click()
    yield driver1
    driver1.quit()
@allure.epic("管理员")
@allure.feature("用户")
@allure.story("添加用户")
@pytest.mark.parametrize('test',yaml.safe_load(open(r'D:\project\uiautotest\user.yml',encoding='UTF-8')))
def test_1add_user(driver,test):
    driver.get("http://114.116.97.187:8080/symfony/web/index.php/pim/viewEmployeeList")
    driver.implicitly_wait(10)
    driver.find_element_by_id("btnAdd").click()
    driver.find_element_by_id('firstName').send_keys(test['firstName'])
    driver.find_element_by_id('lastName').send_keys(test['lastName'])
    driver.find_element_by_id('employeeId').send_keys(test['employeeId'])
@allure.epic("管理员")
@allure.feature("用户")
@allure.story("查询用户")
def test_2inquire_user(driver):
    driver.find_element_by_id("menu_pim_viewEmployeeList").click()
    driver.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[2]/td[2]/a').click()
@allure.epic("管理员")
@allure.feature("用户")
@allure.story("修改用户")
def test_3modification_user(driver):
    driver.find_element_by_id("btnSave").click()
    driver.find_element_by_id('personal_txtEmpLastName').send_keys('王帅')
    driver.find_element_by_id("btnSave").click()
@allure.epic("管理员")
@allure.feature("用户")
@allure.story("删除用户")
def test_4delete_user(driver):
    driver.find_element_by_id("menu_pim_viewEmployeeList").click()
    driver.find_element_by_id("ohrmList_chkSelectRecord_122").click()
    driver.find_element_by_id("btnDelete").click()
    driver.find_element_by_id("dialogDeleteBtn").click()






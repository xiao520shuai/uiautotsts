from selenium import webdriver
import pytest,time
from object.pages.login_page import Login

@pytest.fixture(scope="session")
def driver():
    driver1 = webdriver.Chrome(executable_path=r"D:\project\object\pages\chromedriver.exe")
    yield driver1
    time.sleep(2)
    driver1.quit()

@pytest.mark.parametrize('data',['777@qq.com','777@qq.com'])
def test_login(driver,data):
    login_page = Login(driver)
    driver.get("http://121.4.36.2:3000//#/login")
    login_page.popclick()
    login_page.input_email(data)
    login_page.input_password("123456")
    login_page.one_click()
    login_page.quite_qiute()
    # assert 'Add to Basket' in login_page.assert_login_success()
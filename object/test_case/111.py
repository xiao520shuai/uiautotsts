from selenium import webdriver
import yaml
import time
import pytest

@pytest.fixture(scope="session")
def driver():
    driver1=webdriver.Chrome(executable_path=r"D:\project\object\pages\chromedriver.exe")

    yield driver1
    time.sleep(3)
    driver1.quit()


def test_2add_jobTitle(driver):
    driver.get("http://114.116.97.187:8001/#/login")
    driver.find_element_by_xpath("//*[@id='mat-dialog-0']/app-welcome-banner/div/div[2]/button[2]/span[1]/span").click()
    driver.find_element_by_id("email").send_keys("777@qq.com")
    driver.find_element_by_id('password').send_keys("123456")
    driver.find_element_by_id("loginButton").click()
    driver.find_element_by_id("navbarAccount").click()
    driver.find_element_by_id("navbarLogoutButton").click()
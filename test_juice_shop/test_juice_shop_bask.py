from selenium import webdriver
import time
import pytest
import yaml
import allure
from selenium.webdriver.support.select import Select
#登陆
driver = webdriver.Chrome(executable_path=r"D:\project\uiautotest\chromedriver.exe")
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("Bitnami.12345")
driver.find_element_by_id("btnLogin").click()
driver.get("http://114.116.97.187:8080/symfony/web/index.php/pim/viewEmployeeList")
driver.implicitly_wait(10)
#添加
driver.find_element_by_id("btnAdd").click()
driver.find_element_by_id('firstName').send_keys('帅')
driver.find_element_by_id('lastName').send_keys('a王')
driver.find_element_by_id('employeeId').send_keys('0002')
driver.find_element_by_id("btnSave").click()
#查询
driver.find_element_by_id("menu_pim_viewEmployeeList").click()
driver.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[2]/td[2]/a').click()
#修改
driver.find_element_by_id("btnSave").click()
driver.find_element_by_id('personal_txtEmpLastName').send_keys('王帅')
driver.find_element_by_id("btnSave").click()
#删除
driver.find_element_by_id("menu_pim_viewEmployeeList").click()
driver.find_element_by_id("ohrmList_chkSelectRecord_121").click()
driver.find_element_by_id("btnDelete").click()
driver.find_element_by_id("dialogDeleteBtn").click()
import exercise.demo


import yaml
import pytest
import allure
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path=r"D:\project\uiautotest\chromedriver.exe")
@allure.feature("登陆")
@pytest.fixture(scope="module",autouse=True)
def login():
    print("登陆")
    yield
    print("退出")
# 把要提前初始化执行的方法的名字通过参数传到这里就行了。
@allure.epic("管理员")
@allure.feature("职称")
@allure.story("添加职称")
@pytest.mark.parametrize('data1',yaml.safe_load(open(r"D:\project\uiautotest\test_data.yml")))
# @pytest.mark.parametrize('data1',yaml.safe_load(open("test_data1.yml",encoding='utf-8')))
def test_add_job(data1):
    with allure.step("1、点击添加职称按钮"):
        print("添加职称"+data1['title'])
    with allure.step("2、输入职称"):
        print("添加职称"+data1['desc'])
@allure.epic("管理员")
@allure.feature("职称")
@allure.story("编辑职称")
def test_first():
    allure.attach("这是需要编辑的点")
    print("绩效")
    # driver.save_screenshot("job1.png")
    # allure.attach.file("job1.png",attachment_type=allure.attachment_type.PNG)
    assert 3==3
@allure.epic("管理员")
@allure.feature("职称")
@allure.story("删除职称")
# @pytest.mark.usefixtures("login")
@allure.issue("http://114.116.97.187:8086/zentao/bug", "断言失败-职称名称超长保存失败")
@allure.testcase("http://114.116.97.187:8086/zentao/")
def test_add_user():
    print("添加用户")
    allure.attach('<head></head><body>这个是执行无效数据</body>', '这是错误页的结果信息', allure.attachment_type.HTML)
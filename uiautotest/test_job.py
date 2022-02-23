import pytest
@pytest.fixture(scope='module',autouse=True)
def login():
    print('登陆')
    yield
    print('退出')
@pytest.mark.parametrize('data1',[{"name":'11',"use":'22',"vaue":'33',},{"name":'111',"use":'222',"vaue":'333',}])
def test_add_job(data1):
    print(data1['name'])
def test_first():
    print('首页')
def test_add_user():
    print('添加用户')

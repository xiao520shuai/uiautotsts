import requests

def test_inter():
    url='http://114.116.97.187:8001/rest/user/login'
    data={"email":"777@qq.com","password":"123456"}
    res=requests.post(url=url,json=data)
    assert 200==res.status_code
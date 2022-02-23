# actionID=&hdnUserTimeZoneOffset=8&installation=&
# _csrf_token=53af69d7f16c263a6ec84bc655269d85&
# txtUsername=admin&txtPassword=Bitnami.12345&Submit=%E7%99%BB%E5%BD%95

login_url='http://114.116.97.187:8080/symfony/web/index.php/auth/login'
import requests,re
login_first_res=requests.get(login_url)
token=re.findall(r'name="_csrf_token" value="(.+?)" id="csrf_token" />', login_first_res.text)[0]
print(token)

post_url='http://114.116.97.187:8080/symfony/web/index.php/auth/validateCredentials'
post_data={
    "_csrf_token":token,
    "txtUsername":"admin",
    "txtPassword":"Bitnami.12345",
    "Submit":"%E7%99%BB%E5%BD%95"
}
res=requests.post(post_url,post_data)
assert 'admin' in res.text
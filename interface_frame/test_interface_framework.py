import requests,yaml,pytest
@pytest.mark.parametrize("pa_data",yaml.safe_load(open('data.yml',encoding='UTF-8')))
def test_juice(pa_data):
    print(pa_data)
    method = pa_data['method']
    url = pa_data['url']
    headers = pa_data['hearders']
    payload = pa_data['payload']
    result = pa_data['result']
    res=requests.request(method=method,url=url,json=payload,headers=headers)
    print(res.text)
    assert result['status_code']==res.status_code
    assert result['message'] in res.text












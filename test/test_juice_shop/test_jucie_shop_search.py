import requests
from unittest import TestCase
class TestAdd(TestCase):
    url = 'http://121.4.36.2:3000/rest/products/search?q=apple'
    a = requests.get(url)
    assert 'apple' in a.text

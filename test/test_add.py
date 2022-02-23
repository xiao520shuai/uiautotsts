from unittest import TestCase
from  unitest_demo.adnum import add

class TestAdd(TestCase):

    def test_add(self):
        assert 7==add(3,4)
        assert 8.3==add(3.5,4.8)
        assert 'a1'==add('a','1')
        assert '王帅'==add('王','帅')
        assert '1帅'==add('1','帅')
        assert '  '==add(' ',' ')

# from exercise.demo import sort_num
# # from unittest import TestCase
# # class TestSort_num(TestCase):
# #     def test_sort_num_negative(self):
# #         result=sort_num(0,0)
# #         assert  result==0
# #     def test_sort_num_zero(self):
# #         result=sort_num(2,0)
# #         assert  result==2
# #     def test_sort_num_1(self):
# #         result=sort_num(2,1)
# #         assert  result==10
# #     def test_sort_num_other(self):
# #         result=sort_num(2,2)
# #         assert  result==20
# # if __name__ == '__main__':
# #     pass
import unittest
from ddt import ddt, data, unpack
@ddt
class TestDdt(unittest.TestCase):
    def setUp(self):
        print("setUp!")
    def tearDown(self):
        print("tearDown!")
    @data([1, 2, 3, 4], [5, 6, 7, 8])
    def test_single_list(self,value):
        print(value[0])
#     @unpack
#     def test_single_list(self, value1, value2, value3, value4):
#         print(value1, value2, value3, value4)
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
from demo import Do_Work
import HTMLReport
from ddt import ddt,data
@ddt
class TestDo_Work(unittest.TestCase):
    @data((4,6,5,1.53),(2,5,15,0),(5,5,5,1.9),(4,5,15,1.48))
    def test_do_Work(self,v):
        result =Do_Work(v[0],v[1],v[2])
        assert v[3]==round(result,2)#全真
    # def test_Do_Work1(self):
    #     result1 = Do_Work(2,4,11)
    #     assert result1 == 0#全假
    # def test_Do_Work2(self):
    #     result2 = Do_Work(6,3,7)
    #     assert result2 == 1.1231056256176606#执行第二个
    # def test_Do_Work3(self):
    #     result3 = Do_Work(6,6,6)
    #     assert result3 == 1.662757831681574#执行第一个
if __name__ == '__main__':
    # 建立一个套件
    suite=unittest.TestSuite()
    # 建立一个加载器
    loader=unittest.TestLoader()
    # 在套件中通过名字加载测试用例
    suite.addTest(loader.loadTestsFromName("test_do_Work"))
    # 定制报告模板
    runner = HTMLReport.TestRunner(report_file_name="oracle 华育兴业单元测试功能测试报告",
                                    output_path="report",
                                    title="演示功能测试",
                                   description="这是个练习而已",
                                   lang="cn"
                                   )
    # 执行测试用例套件
    runner.run(suite)

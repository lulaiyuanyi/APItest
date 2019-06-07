import unittest

class TestWinner(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        print("全部用例执行之后")

    @classmethod
    def setUpClass(cls):
        print("全部用例之前，只准备一次")


    # def setUp(self):
    #     print("每条测试用例之前都会执行")
    #     print("数据准备工作，准备需要的数据")
    #
    # def tearDown(self):
    #     print('每个测试用例之后都会执行')
    #     print('数据清理：清理测试产生的垃圾数据，不影响后面的用例')
    def test_0A(self):
        print("测试用例test_0A")

    def test_01(self):
        print("测试用例test_01")

    def test_0a(self):
        print("测试用例test_0a")

    def test_02(self):
        print("测试用例test_02")

if __name__ == '__main__':
    unittest.main()
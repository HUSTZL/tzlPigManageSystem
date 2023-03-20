import unittest

from src.main import Search
from src.main import Buy

class test_Search(unittest.TestCase):
    # 创建测试用例方法, 方法要以test开头
    # 执行顺序是根据case序号来的, 并非代码的顺序
    def setUp(self) -> None:  # 调用setUp
        super().setUp()
        print("测试用例执行前操作")

    def tearDown(self) -> None:  # 调用tearDown
        super().tearDown()
        print("测试用例执行后操作")

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        print("测试前的操作")

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        print("测试后的操作")

    def test_add_01(self):
        print(3 + 2)

    def test_add_02(self):
        print(10 + 5)

    def test_add_03(self):
        print("1 == 1")
        self.assertEqual(1, 1)  # 成功

    def test_add_04(self):
        print("1 == 2")
        self.assertEqual(1, 2)  # 失败

    def test_add_05(self):
        print("1 !=2 ")
        self.assertNotEqual(1, 2)  # 成功

    def test_add_06(self):
        print("1 != 1")
        self.assertNotEqual(1, 1)  # 失败
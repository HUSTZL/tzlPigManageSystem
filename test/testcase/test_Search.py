import unittest
import os

from src.main import Search, Buy


class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cmd = "python /home/lmc20020909/项目/tzlPigManageSystem/src/rebuild_database.py"
        res = os.system(cmd)
        # print(res)
        buy = Buy()
        buy.run(100000, "Black", "3", "0")
        # print("测试前的操作")

    # 查询不存在的猪
    def test_search_01(self):
        search = Search()
        res = search.run("0", "3")
        # print("Pig not exist")
        self.assertEqual(res, "Pig not exist")

    # 查询存在的猪
    def test_search_02(self):
        search = Search()
        res = search.run("0", "0")
        # print(res)
        self.assertEqual(res.pigId, 0)
        self.assertEqual(res.type, "Black")
        self.assertTrue(20 <= res.weight <= 50)

    # 查询有猪的Farm
    def test_search_03(self):
        search = Search()
        res = search.run("1", "0")
        self.assertEqual(res.FarmId, 0)
        self.assertEqual(res.Remain, 7)

    # 查询没猪的Farm
    def test_search_04(self):
        search = Search()
        res = search.run("1", "99")
        self.assertEqual(res.FarmId, 99)
        self.assertEqual(res.Remain, 10)

    # 查询不存在的Farm
    def test_search_05(self):
        search = Search()
        res = search.run("1", "100")
        self.assertEqual(res, "Farm not exsit")

    # 不合法输入_the first parameter is not a digit
    def test_search_06(self):
        search = Search()
        res = search.run("fuck", "1")
        self.assertEqual(res, "input wrong")

    # 不合法输入_the first parameter is a digit but not in {0, 1}
    def test_search_07(self):
        search = Search()
        res = search.run("2", "1")
        self.assertEqual(res, "input wrong")

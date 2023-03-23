import unittest
import os

from src.main import Search, Buy


class TestSearch(unittest.TestCase):

    tmp = None

    def setUp(self) -> None:
        super().setUp()
        global tmp
        cmd = "python /home/lmc20020909/项目/tzlPigManageSystem/src/rebuild_database.py"
        res = os.system(cmd)
        # print(res)
        buy = Buy()
        tmp = buy.run(100000, "Black", "3", "0")

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        # print("测试前的操作")

    # 买一只Small Pig
    def test_buy_01(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Small", "1", "3")
        self.assertTrue(mon - 7 * 50 <= tmp[0] <= mon - 7 * 20)
        self.assertEqual(tmp[1], [1])

    # 买一只Big Pig
    def test_buy_02(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Big", "1", "3")
        self.assertTrue(mon - 6 * 50 <= tmp[0] <= mon - 6 * 20)
        self.assertEqual(tmp[1], [1])

    # 买一只Black Pig
    def test_buy_03(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Black", "1", "3")
        self.assertTrue(mon - 15 * 50 <= tmp[0] <= mon - 15 * 20)
        self.assertEqual(tmp[1], [0])

    # 买15只Small Pig，买3只Black Pig，买16只Big Pig
    def test_buy_04(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Small", "15", "3")
        self.assertTrue(mon - 7 * 15 * 50 <= tmp[0] <= mon - 7 * 15 * 20)
        self.assertEqual(tmp[1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Black", "3", "18")
        self.assertTrue(mon - 15 * 3 * 50 <= tmp[0] <= mon - 15 * 3 * 20)
        self.assertEqual(tmp[1], [0, 0, 0])
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Big", "15", "21")
        self.assertTrue(mon - 6 * 15 * 50 <= tmp[0] <= mon - 6 * 15 * 20)
        self.assertEqual(tmp[1], [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])

    # 参数a输入非法
    def test_buy_05(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "hhforz", "15", "3")
        self.assertEqual(tmp[1], "input wrong")

    # 参数b输入非法
    def test_buy_06(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Black", "hhforz", "3")
        self.assertEqual(tmp[1], "input wrong")

    # 参数startno输入非法
    def test_buy_07(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(tmp[0], "Small", "15", "hhforz")
        self.assertEqual(tmp[1], "input wrong")

    # 余额不足
    def test_buy_08(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(0, "Small", "15", "3")
        self.assertEqual(tmp[1], "money not enough")

    # # 猪的编号冲突
    # def test_buy_09(self):
    #     global tmp
    #     buy = Buy()
    #     mon = tmp[0]
    #     tmp = buy.run(tmp[0], "Small", "15", "1")
    #     self.assertEqual(tmp[1], "startno conflict")

    # farm满
    def test_buy_10(self):
        global tmp
        buy = Buy()
        mon = tmp[0]
        tmp = buy.run(1000000, "Big", "1000", "3")
        self.assertEqual(tmp[1], "farm not enough")
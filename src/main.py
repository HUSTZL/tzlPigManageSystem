import sqlite3
from src.property.Pig import Pig
from src.property.Farm import Farm
import numpy as np

'''
    Pig (
        PigId INT PRIMARY KEY,
        Type CHAR(10),
        Weight INT,
        Age INT,
        IsSick INT,
        FarmId INT,
        FOREIGN KEY(FarmId) REFERENCES Farm(FarmId)
    )
     Black, Small, Big

    Farm (
        FarmId INT PRIMARY KEY,
        Remain INT
    )
    
    Money (
        Remain INT PRIMARY KEY
    )
'''

class Search():
    def __init__(self):
        return

    def run(self, a, Id):
        if a.isdigit():
            if a == "0":
                if Id.isdigit():
                    data = []
                    con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Pig WHERE PigId = {}".format(a))
                    infos = cur.fetchall()
                    cur.close()
                    con.close()

                    for row in infos:
                        pig = Pig(row[0], row[1], row[2], row[3], row[4], row[5])
                        data.append(pig)
                    if len(data) == 0:
                        return "Pig not exist"
                    else:
                        return str(data[0])
                else:
                    return "input wrong"
            elif a == "1":
                if Id.isdigit():
                    data = []
                    con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                    cur = con.cursor()
                    cur.execute("SELECT * FROM Farm WHERE FarmId = {}".format(a))
                    infos = cur.fetchall()
                    cur.close()
                    con.close()
                    for row in infos:
                        farm = Farm(row[0], row[1])
                        data.append(farm)
                    if len(data) == 0:
                        return "Farm not exsit"
                    else:
                        return str(data[0])
                else:
                    return "input wrong"
            else:
                return "input wrong"
        else:
            return "input wrong"

class Buy():
    def __init__(self):
        return

    def run(self, mon, a, b, startno):
        if str(mon).isdigit() and (a == 'Black' or a == 'Small' or a == 'Big') and b.isdigit() and startno.isdigit():
            n = int(b)
            startno = int(startno)
            initW = np.random.random(n) * 30 + 20
            totInitW = sum(initW)
            resultpig = []
            if (a == 'Black' and 15 * totInitW <= mon) or (a == 'Small' and 7 * totInitW <= mon) or (a == 'Big' and 6 * totInitW <= mon):

                con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM Pig")
                pigs = []
                infos = cur.fetchall()
                for row in infos:
                    pig = Pig(row[0], row[1], row[2], row[3], row[4], row[5])
                    pigs.append(pig)
                cur.close()
                con.close()

                con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM Farm")
                farms = []
                remainpig = [0 for i in range(1000)]
                infos = cur.fetchall()
                for row in infos:
                    farm = Farm(row[0], row[1])
                    remainpig[row[0]] = row[1]
                    farms.append(farm)
                cur.close()
                con.close()

                count = 0
                for w in initW:
                    count += 1
                    flag = 0
                    for i in range(0, 100):
                        if remainpig[i] == 10:
                            flag = 1
                            resultpig.append(i)
                            remainpig[i] -= 1
                            pigs.append(Pig(startno + count - 1, a, w, 0, 0, i))
                            break
                        elif remainpig[i] < 10 and remainpig[i] >= 1:
                            flag1 = -1
                            for pig in pigs:
                                if pig.farmId == i:
                                    if (pig.type == "Black" and a != "Black") or (pig.type != "Black" and a == "Black"):
                                        continue
                                    else:
                                        flag1 = i
                                        break
                            if flag1 != -1:
                                pigs.append(Pig(startno + count - 1, a, w, 0, 0, flag1))
                                resultpig.append(flag1)
                                remainpig[flag1] -= 1
                                flag = 1
                                break
                    if flag == 0:
                        return mon, "farm not enough"

                mon -= (a == 'Black') * (15 * totInitW) + (a == 'Small') * (7 * totInitW) + (a == 'Big') * (6 * totInitW)

                con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                cur = con.cursor()
                for i in range(n):
                    no = startno + i
                    cur.execute("Insert INTO Pig(PigId, Age, Weight) VALUES({}, {}, {})".format(no, 0, initW[i]))
                con.commit()
                cur.close()
                con.close()

                con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                cur = con.cursor()
                for i in range(100):
                    cur.execute("Update Farm SET Remain = {} WHERE FarmId = {}".format(remainpig[i], i))
                con.commit()
                cur.close()
                con.close()

                return mon, resultpig
            else:
                return mon, "money not enough"
        else:
            return mon, "input wrong"

class UI():
    def __init__(self):
        return

    def run(self):
        while True:
            print("这是养猪场管理系统：\n 输入1：查询 \n 输入2 采购猪")
            a = input()
            if a.isdigit():
                if a == "1":
                    print("Please input Pig(0)/Farm(1), PigId/FarmId in a row")
                    b = input().split(' ')
                    if len(b) == 2:
                        search = Search()
                        print(search.run(b[0], b[1]))
                    else:
                        print("input wrong")
                elif a == "2":
                    print("Please input Black/Small/Big, number, start_no in a row")
                    b = input().split(' ')
                    if len(b) == 3:
                        con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                        cur = con.cursor()
                        cur.execute("SELECT * FROM Money")
                        infos = cur.fetchall()
                        remain_mon = infos[-1][0]
                        cur.close()
                        con.close()

                        buy = Buy()
                        resultmon, resultpig = buy.run(remain_mon, b[0], b[1], b[2])
                        print(resultmon, resultpig)

                        con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
                        cur = con.cursor()
                        cur.execute("UPDATE MONEY SET Remain = {} WHERE Remain = {}".format(resultmon, remain_mon))
                        con.commit()
                        cur.close()
                        con.close()
                    else:
                        print("input wrong")
                else:
                    print("input wrong")
            else:
                print("input wrong")


if __name__ == '__main__':
    ui = UI()
    ui.run()

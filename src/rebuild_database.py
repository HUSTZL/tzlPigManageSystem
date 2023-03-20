import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect('/home/moonlight/PigManageSystem/database/data.db')
    cur = con.cursor()
    cur.execute("DELETE FROM Pig")
    cur.execute("DELETE FROM Farm")
    cur.execute("DELETE FROM Money")
    for i in range(100):
        cur.execute("INSERT INTO FARM VALUES({}, 10)".format(i))
    cur.execute("INSERT INTO Money VALUES(100000)")
    con.commit()
    cur.close()
    con.close()
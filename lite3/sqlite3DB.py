import sqlite3
def create_table(tablename):
    # try:
        con = sqlite3.connect('test2.db')
        # con = pymysql.connect(host='localhost', user='root',
        #                       passwd='mgq960830!', charset='utf8')
        cur = con.cursor()

        # cur.execute("create database {tablename};".format(tablename = tablename))

        # cur.execute("use {tablename};".format(tablename = tablename))

        cur.execute("CREATE TABLE IF NOT EXISTS test ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "name varchar(50) NOT NULL,"
                    "bit char(20),"
                    "numK char(20),"
                    "tidW char(20),"
                    "tidN char(20),"
                    "subTidW char(20),"
                    "subTidN char(20),"
                    "sTypeW_bit varchar(50),"
                    "sType char(20),"
                    "storeLocation varchar(50),"
                    "algoId char(20),"
                    "algoSpe char(20),"
                    "testSpe char(20),"
                    "castType char(20),"
                    "iOrd char(20),"
                    "TBLM_ID varchar(50),"
                    "dpt char(20),"
                    "dpt_person varchar(50),"
                    "confirmation varchar(50)"
                    ");")
    # except Exception as e:
    #     raise e
    # finally:
        con.close()
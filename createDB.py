import pymysql

def create_tale(tablename):
    try:

        con = pymysql.connect(host='localhost', user='root',
                              passwd='mgq960830!', charset='utf8')
        cur = con.cursor()

        cur.execute("create database {tablename};".format(tablename = tablename))

        cur.execute("use {tablename};".format(tablename = tablename))

        cur.execute("CREATE TABLE IF NOT EXISTS {tablename} ("
                    "id INT UNSIGNED AUTO_INCREMENT,"
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
                    "tidName varchar(50),"
                    "TBLM_ID varchar(50),"
                    "dpt char(20),"
                    "dpt_person varchar(50),"
                    "confirmation varchar(50),"
                    "PRIMARY KEY (id)"
                    ");".format(tablename = tablename))
    except Exception as e:
        raise e
    finally:
        con.close()
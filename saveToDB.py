import pymysql
import connectDB
import openpyxl
import xlsxOpenpyxl
import insertDB
import lite3.sqlite3DB


def save_DB(lists, tablename):
    # try:
    # db = connectDB.connect_db('localhost', 'root', 'mgq960830!', '5885ce76mb')

    # lists = xlsxOpenpyxl.read_excel_xlsx(tablename, 'Sheet1')

    for i in lists:
        i[0] = int(i[0])
        print(i)
        insertDB.insert_db(tablename, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12],
                           i[13],
                           i[14],
                           i[15],
                           i[16],
                           i[17],
                           i[18],
                           i[19])
    # cur = db.cursor()
    # cur.execute(sql_quarry)

    # results = cur.fetchall()
    # print("id", "user_id", "name")
    #
    # for row in results:
    #     id = row[0]
    #     user_id = row[1]
    #     name = row[2]
    #     print(id, name, user_id)
    # return results
# except Exception as e:
#     raise e
# finally:
#     db.close()

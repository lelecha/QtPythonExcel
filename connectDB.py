# -*- coding:utf8 -*-
import pymysql
#连接数据库查询
def connect_db(host,username,password,database):

    db = pymysql.connect(host,username,password,database)


    return db
    # sql = "select * from blogs"
    # try:
    #     cur.execute(sql)
    #
    #     results = cur.fetchall()
    #     print("id", "user_id", "name")
    #
    #     for row in results:
    #         id = row[0]
    #         user_id = row[1]
    #         name = row[2]
    #         print(id, name, user_id)
    # except Exception as e:
    #     raise e
    # finally:
    #     db.close()

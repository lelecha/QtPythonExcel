import pymysql
import connectDB
import sqlite3


def quarry_field_name(cur):
    sqlFields = cur.description

    num = len(sqlFields)
    fields = [None] * num

    for i in range(num):
        print(sqlFields[i][0])

        fields[i] = sqlFields[i][0]

    return fields


def get_head_name(tablename):
    db = sqlite3.connect('../test2.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM '{tablename}'".format(tablename=tablename))
    sqlFields = cur.description
    num = len(sqlFields)
    fields = [None] * num
    print(num)
    for i in range(num):
        print(sqlFields[i][0])
        print(i)
        fields[i] = sqlFields[i][0]
    db.close()
    return fields


def quarbry_id(tablename, id):
    sql_quarry = "select * from {tablename} where id = '{id}';".format(tablename=tablename,
                                                                       id=id)
    try:
        db = sqlite3.connect('test2.db')
        # db = connectDB.connect_db('localhost', 'root', 'mgq960830!', 'awesome')
        cur = db.cursor()
        cur.execute(sql_quarry)
        headName = quarry_field_name(cur)
        results = cur.fetchall()
        results.insert(0, headName)
        # print("id", "user_id", "name")
        print(results)
        # for row in results:
        #     id = row[0]
        #     user_id = row[1]
        #     name = row[2]
        #     print(id, name, user_id)
        return results
    except Exception as e:
        raise e
    finally:
        db.close()


def quarry_all(tablename):
    sql_quarry = "select * from '{tablename}';".format(tablename=tablename)
    try:
        db = sqlite3.connect('../test2.db')
        # db = connectDB.connect_db('localhost', 'root', 'mgq960830!', '5885ce76mb')
        cur = db.cursor()
        cur.execute(sql_quarry)
        # headName = quarry_field_name(cur)
        results = cur.fetchall()
        # results.insert(0, headName)
        print(results)
        # for row in results:
        #     id = row[0]
        #     user_id = row[1]
        #     name = row[2]
        #     print(id, name, user_id)
        return results
    except Exception as e:
        raise e
    finally:
        db.close()


# 测试版 最后加入所有条件
def quarry_search(name, bit, numK):
    # dic = {
    #
    #     name: 0,
    #     bit: 1,
    #     numK: 2,
    #
    # }
    list = [None] * 3  # 后期会改
    if bit == '':
        list[1] = '1'
        bit = '1'
    else:
        list[1] = 'bit'

    if numK == '':
        list[2] = '1'
        numK = '1'
    else:
        list[2] = 'numK'

    if name == '':
        list[0] = '1'
        name = '1'
    else:
        list[0] = 'name'
    print(list)
    #还要遍历所有table
    sql_quarry = "select * from {tablename} where {name} = {name_} " \
                 "and {bit} = {bit_} " \
                 "and {numK} = {numK_};".format(tablename = 'test',
                                                 name = list[0],
                                                 name_= name,
                                                 bit = list[1],
                                                 bit_= bit,
                                                 numK = list[2],
                                                 numK_= numK
                                               )
    print(sql_quarry)
    db = sqlite3.connect('../test2.db')
    cur = db.cursor()
    cur.execute(sql_quarry)
    results = cur.fetchall()
    print(results)
    return results
    # sql_quarry = "select * from {tablename} where ;".format(tablename = tablename)
    # try:
    #     db = sqlite3.connect('test2.db')
    #     # db = connectDB.connect_db('localhost', 'root', 'mgq960830!', '5885ce76mb')
    #     cur = db.cursor()
    #     cur.execute(sql_quarry)
    #     headName = quarry_field_name(cur)
    #     results = cur.fetchall()
    #     results.insert(0, headName)
    #     print(results)
    #     # for row in results:
    #     #     id = row[0]
    #     #     user_id = row[1]
    #     #     name = row[2]
    #     #     print(id, name, user_id)
    #     return results
    # except Exception as e:
    #     raise e
    # finally:
    #     db.close()

import pymysql
import connectDB


def delete_db(tablename, id):

    sql_delete = "DELETE FROM {tablename} WHERE id = '{id}';".format(tablename = tablename,id = id,)
    try:
        db = connectDB.connect_db("localhost", "root", "mgq960830!", "5885ce76mb")
        cur_delete = db.cursor()
        cur_delete.execute(sql_delete)
        db.commit()
        print('success delete')
    except Exception as e:
        db.rollback()
        print('rollback')
    finally:
        db.close()

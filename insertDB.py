import pymysql
import connectDB
import lite3.sqlite3DB
import sqlite3


def insert_db(tablename, id, name, bit, numK
              , tidW, tidN, subTidW, subTidN, sTypeW_bit, sType, storeLocation, algoId, algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation):

    sql_insert = "insert into test (id, name, bit, numK, tidW, tidN, subTidW, subTidN, sTypeW_bit, sType, " \
                 "storeLocation, algoId,algoSpe, testSpe, " \
                 "castType, iOrd, TBLM_ID, dpt, dpt_person, confirmation) " \
                 "values ( NULL,'{name}', '{bit}', '{numK}', '{tidW}', '{tidN}', '{subTidW}', " \
                 "'{subTidN}', '{sTypeW_bit}', '{sType}', '{storeLocation}', '{algoId}','{algoSpe}','{testSpe}', " \
                 "'{castType}', '{iOrd}', '{TBLM_ID}', '{dpt}', '{dpt_person}', '{confirmation}');".format(
                                                                                                           name=name,
                                                                                                           bit=bit,
                                                                                                           numK=numK
                                                                                                           , tidW=tidW,
                                                                                                           tidN=tidN,
                                                                                                           subTidW=subTidW,
                                                                                                           subTidN=subTidN,
                                                                                                           sTypeW_bit=sTypeW_bit,
                                                                                                           sType=sType,
                                                                                                           storeLocation=storeLocation,
                                                                                                           algoId=algoId,
                                                                                                           algoSpe=algoSpe,
                                                                                                           testSpe=testSpe,
                                                                                                           castType=castType,
                                                                                                           iOrd=iOrd,
                                                                                                           TBLM_ID=TBLM_ID,
                                                                                                           dpt=dpt,
                                                                                                           dpt_person=dpt_person,
                                                                                                           confirmation=confirmation)

    db = sqlite3.connect('test2.db')
    cur_insert = db.cursor()
    cur_insert.execute(sql_insert)
    db.commit()
    print('success insert')
    # except Exception as e:
    #     db.rollback()
    #     print('rollback')
    # finally:
    db.close()

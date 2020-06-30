# -*- coding:utf8 -*-
import quarryDB
import xlsxOpenpyxl
import os
import deleteDB
import saveToDB
import createDB
import lite3.sqlite3DB

def main():
   # print os.getcwd()
   # insertDB.insert_db('blogs','2','22','tom')
   # #全表 并插入excel
   # result = quarryDB.quarry_all('test')
   # xlsxOpenpyxl.write_excel_xlsx('test.xlsx','Sheet1',result)

   # 存入db
   # lists = xlsxOpenpyxl.read_excel_xlsx('text2.xlsx','Sheet1')
   # saveToDB.save_DB(lists, 'blogs')
   # 删除
   # deleteDB.delete_db('blogs','1')
   # result = quarryDB.quarry_all('blogs')
   # xlsxOpenpyxl.write_excel_xlsx('text2.xlsx', 'Sheet1', result)
   # 实验
   # lite3.sqlite3DB.create_table('5885CE76Mb')
   # lists = xlsxOpenpyxl.read_excel_xlsx('test4.xlsx','Sheet1')
   #
   # saveToDB.save_DB(lists, 'test')
   quarryDB.quarry_search('','','')

if __name__ == '__main__':
    main()
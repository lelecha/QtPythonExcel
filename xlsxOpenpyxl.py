#!/usr/bin/python
# -*- coding:utf8 -*-

import openpyxl


# 提取数据导入新的excel
def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    workbook.save(path)
    print("success")


def write_excel_newLine(path, sheet_name, value):  # 这里的value是新的内容
    # index = len(value)
    list = read_excel_xlsx(path, sheet_name)
    for i in value:
        list.append(i)
    write_excel_xlsx(path, sheet_name, list)
    # for i in range(0, index):
    #     for j in range(0, len(value[i])):
    #         sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    # workbook.save(path)
    print("insert new line into excel")


def read_excel_xlsx(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    lists = []
    sheet = workbook[sheet_name]
    for row in sheet.values:
        temp = list(row)
        for i in range(len(temp)):
            temp[i] = str(temp[i])
        lists.append(temp)
    del (lists[0])
    print(lists)
    return lists
    # for j in row:
    #     print(j)

    # list = tuple(sheet.rows)
    # print('111')

    # for row in sheet.rows:
    #     for cell in row:
    #         print(cell.value, "\t")
    #     print()

# book_name_xlsx = 'text2.xlsx'
#
# sheet_name_xlsx = 'xlsxformtest'
#
# value3 = [["姓名", "性别", "年龄", "城市", "职业"],
#           ["111", "女", "66", "石家庄", "运维工程师"],
#           ["222", "男", "55", "南京", "饭店老板"],
#           ["333", "女", "27", "苏州", "保安"], ]
#
# write_excel_xlsx(book_name_xlsx, sheet_name_xlsx, value3)

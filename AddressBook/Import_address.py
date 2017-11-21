# !/usr/bin/python
# —*— coding: UTF-8 —*—
import os,sys
import pymysql

connect = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'twd123456',
    db = 'twd',
    charset = 'utf8'
)

cursor = connect.cursor()

def import_address():
    sql = "SELECT COUNT(1) from twd.mydata"
    cursor.execute(sql)
    for row in cursor.fetchall():
        pass
    path = os.getcwd()
    print(path)
    FileOpen = open(path + '/test/AddressBookaddress.csv', 'r')
    for importrow in FileOpen:
        importnewkey =tuple(importrow)
        pass

    #     importkey = [0, 'a', 'a', 0, 'a', 'a','a']
    #     importtmp = row[0] + 1
    #     importkey[0] = importtmp
    #     importkey[1] = import[0]
    #     importkey[2] = importrow[1]
    #     importkey[3] = importrow[2]
    #     importkey[4] = importrow[3]
    #     importkey[5] = importrow[4]
    #     importkey[6] = importrow[5]
    #

a = import_address()


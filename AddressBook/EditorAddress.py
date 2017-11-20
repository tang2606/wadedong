# !/usr/bin/python
# —*— coding: UTF-8 —*—
import pymysql.cursors
import print_message
import os


connect = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'twd123456',
    db = 'twd',
    charset = 'utf8'
)

cursor = connect.cursor()



#查询联系人
def Query_address():
    print_message.print_cxmenu()
    while True:
        cxkey = int(input("\n请选择要查询的方式："))
        if cxkey == 1:
            cxuseridkey = [0]
            cxuseridkey[0] = int(input('请输入编号：'))
            sql = "SELECT * from twd.mydata WHERE id='%d'"
            data = tuple(cxuseridkey)
            cursor.execute(sql % data)
            for row in cursor.fetchall():
                print("查询结果为：")
                print(row)

        elif cxkey == 2:
            cxnamekey = ['a']
            cxnamekey[0] = input("\n请输入要查询姓名：")
            sql = "SELECT * from twd.mydata WHERE name='%s'"
            data = tuple(cxnamekey)
            cursor.execute(sql % data)
            for row in cursor.fetchall():
                print("\n查询结果为：")
                print(row)
        elif cxkey == 3:
            cxsex = []
            cxsexkey = int(input("\n请输入查询的性别_男(1)、女(2)："))
            if cxsexkey == 1:
                cxsex = ['男']
            elif cxsexkey == 2:
                cxsex = ['女']
            else:
                print('\n本系统只支持男女性别！！！')
                continue
            sql = "SELECT * from twd.mydata WHERE sex='%s'"
            data = tuple(cxsex)
            cursor.execute(sql % data)
            for row in cursor.fetchall():
                print(row)

        elif cxkey == 4:
            cxagekey = ['a']
            cxagekey[0] = int(input("请输入查询的年龄："))
            sql = "SELECT * from twd.mydata WHERE age='%d'"
            data = tuple(cxagekey)
            cursor.execute(sql % data)
            cxage = ()
            for row in cursor.fetchall():
                cxage = row
            if cxage.__contains__(data[0]) == True :
                print("查询结果为：")
                print(cxage)
            else:
                print('\n没有这个年龄的联系人！！！')

        elif cxkey == 5:
            cxagekey = ['a']
            cxagekey[0] = input("\n请输入查询的手机号：")
            sql = "SELECT * from twd.mydata WHERE mobile='%s'"
            data = tuple(cxagekey)
            cursor.execute(sql % data)
            cxmobile = ()
            for row in cursor.fetchall():
                cxmobile = row
            if cxmobile.__contains__(data[0]) == True:
                print('查询结果')
                print(cxmobile)
            else:
                print('\n没有这个手机号的联系人！！！')


        elif cxkey == 6:
            print("查询结果为：")
            sql = "SELECT * from twd.mydata"
            cursor.execute(sql)
            for row in cursor.fetchall():
                print(row)

        elif cxkey == 7:
            print_message.Qc_Clear()
        elif cxkey == 8:
            break
        else:
            print("输入错误，请重新输入：")




#修改联系人信息
def Update_Address():
    updatekey = [1, 'a', 'a', 1]
    updatekey[3] = int(input("请输入需要修改的id："))
    print("只能修改年龄、地址、省份")
    updatekey[0] = int(input("请输入年龄："))
    updatekey[1] = input("请输入地址：")
    updatekey[2] = input("请输入省份：")
    sql = "UPDATE twd.mydata SET age='%d',address='%s',province='%s' WHERE id='%d';"
    data = tuple(updatekey)
    cursor.execute(sql % data)
    connect.commit()  # 提交修改
    cursor.close()
    connect.close()


#新增联系人
def Insert_Address():
    sql = "SELECT COUNT(1) from twd.mydata"
    cursor.execute(sql)
    for row in cursor.fetchall():
        pass
    insertkey = [0, 'a', 'a', 0, 'a', 'a','a']
    inserttmp = row[0] + 1
    insertkey[0] = inserttmp
    insertkey[1] = input('请输入联系人姓名：')
    insertkey[2] = input('请输入联系人性别：')
    insertkey[3] = int(input('请输入联系人年龄：'))
    insertkey[4] = input('请输入联系人手机号：')
    insertkey[5] = input('请输入联系人地址：')
    insertkey[6] = input('请输入联系人省份：')
    sqlmobile = "SELECT mobile from twd.mydata WHERE mobile = '%s'"
    detamobile = insertkey[4]
    cursor.execute(sqlmobile % detamobile)
    sqlmobiletxt = ()
    for sqlmobile_i in cursor.fetchall():
        sqlmobiletxt = sqlmobile_i
    if sqlmobiletxt.__contains__(insertkey[4]) == True:
        print('\n该手机号已经存在,请重新输入：')
    else:
        sql = "INSERT INTO twd.mydata(`id`, `name`, `sex`, `age`,`mobile`, `address`, `province`) VALUES('%d', '%s', '%s', '%d', '%s','%s', '%s');"
        data = tuple(insertkey)
        cursor.execute(sql % data)
        print(cursor.execute())
        connect.commit()  # 提交修改
        print('\n添加成功！！！')
        cursor.close()
        connect.close()

#导出联系人
def Export_All():
    the_pwd = os.getcwd()
    file_name = input('请输入导出文件名：')
    file_pwd = the_pwd
    f = open(file_pwd + file_name + '.csv', 'w', encoding='utf_8_sig')
    list_name = ['用户id,', '姓名,', '性别,', '年龄,', '手机号,', '地址,', '籍贯']
    f.writelines(list_name)
    f.writelines('\n')
    f.close()

    sql = "SELECT * from twd.mydata"
    cursor.execute(sql)
    for row in cursor.fetchall():
        f = open(file_pwd + file_name + '.csv', 'a', encoding='utf_8_sig')
        f.writelines(row[0].__str__() + ',')
        f.writelines(row[1].__str__() + ',')
        f.writelines(row[2].__str__() + ',')
        f.writelines(row[3].__str__() + ',')
        f.writelines(row[4].__str__() + ',')
        f.writelines(row[5].__str__() + ',')
        f.writelines(row[6].__str__())
        f.writelines('\n')
        f.close()

    cursor.close()
    connect.close()
    return True

def Del_address():
    print('为了保证数据安全，删除需要同时输入姓名和手机号：')
    delkey = ['a','a']
    delkey[0] = input('\n输入要删除的联系人姓名：')
    delkey[1] = input('输入要删除的联系人手机：')
    sql = "DELETE FROM twd.mydata WHERE name = '%s' AND mobile = '%s'"
    data = tuple(delkey)
    cursor.execute(sql % data)
    connect.commit()  # 提交修改
    print('\n删除成功！！！')
    cursor.close()
    connect.close()


# !/usr/bin/python
# -*- coding: UTF-8 -*-
'''
mast
'''
import pymysql.cursors
import os
import time
import print_message
import EditorAddress

while True:
    print_message.print_menu()
    runkey = int(input("\n请输入需要的操作编号："))
    if runkey == 1:
        EditorAddress.Query_address()
        # 查询联系人
    elif runkey == 2:
        EditorAddress.Update_Address()
        # 更新联系人
    elif runkey == 3:
        EditorAddress.Insert_Address()
        # 插入联系人

    elif runkey == 4:
        EditorAddress.Del_address()
        # 删除联系人
    elif runkey == 5:
        # 导出联系人
        return_key = EditorAddress.Export_All()
        if return_key == True:
            print('\n导出成功！！！！')
        else:
            print('导出失败')
    elif runkey == 6:
        break
    elif runkey == None:
        break
    else:
        print("请输入正确的选项！！！\n \n")

print('\n     结束！！')
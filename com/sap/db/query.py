#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM USER \
        WHERE ID = '%d'" % (2)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表

    # print("cursor.rowcount:"+cursor.rowcount)

    rs = cursor.fetchone()

    print(rs)

    rs = cursor.fetchmany(3)

    print(rs)

    rs = cursor.fetchall()

    print(rs)

except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()

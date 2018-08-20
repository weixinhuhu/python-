import pymysql
import 高级.数据库.数据库连接 as mydb
_author_ = 'weixin'
# 打开数据库连接
cursor =mydb.MySql.connect("mysql")#建表语句
sql= """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
#如果表存在删除
cursor.execute("drop  table if exists EMPLOYEE")
#执行建表语句
cursor.execute(sql)
cursor.close()



import 高级.数据库.数据库连接 as MySql
db = MySql.MySql.connect()
cursor=db.cursor()
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 500)"""
cursor.execute(sql)
db.commit()
print("插入数据成功！")
# 关闭数据库连接
db.close()

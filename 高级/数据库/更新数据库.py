import 高级.数据库.数据库连接 as MySql
db = MySql.MySql.connect()
cursor=db.cursor()

# SQL 更新语句高级/数据库/数据库连接.py:11
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()

   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
      print("修改数据成功")

except:
   print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()
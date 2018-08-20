import pymysql as mysql
class MySql():
        @staticmethod
        def connect():
            config={'host':'localhost',#默认127.0.0.1
                    'user':'root',
                    'password':'12345678',
                    'port':3306,#默认即为3306
                    'database':'Test',
                    'charset':'utf8'#默认即为utf8
                    }
            try:
                cnn=mysql.connect(**config)#connect方法加载config的配置进行数据库的连接，完成后用一个变量进行接收
            except mysql.connector.Error as e:
                print('数据库链接失败！',str(e))
                cnn.close()
            else:#try没有异常的时候才会执行
                print("Connect MysqlDB sucessfully!")
                return cnn
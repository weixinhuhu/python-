import pandas as pd
import 高级.数据库.数据库连接 as MySql
import ssl

# 当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出该错误消息。
ssl._create_default_https_context = ssl._create_unverified_context

# 读取网络端csv文件
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

try:
    df = pd.read_csv(data_url)
    # 打印数据前五行
    print(df.head())
    # 打印数据后五行
    print(df.tail())
    # 打印10~20行前三列数据
    print(df.iloc[10:20,0:3])
    # 提取不连续行和列的数据，这个例子提取的是第1,2,4行，第2,4列的数据
    print(df.iloc[[1,2,4],[2,4]])
except Exception as e:
    print(e)

# # 读取数据库数据
# try:
#     db = MySql.MySql.connect()
#     df = pd.read_sql('SELECT * FROM Test.EMPLOYEE',con=db)
#     print(df)
#     # 数据到处到csv文件
#     # index=False表示导出时去掉行名称，如果数据中含有中文，一般encoding指定为‘utf-8’
#     df.to_csv('./demo.csv',encoding='utf-8',index=False)
#     db.close()
# except Exception as e:
#     print(e)

# 读取excel文件本地文件
# try:
#     df = pd.read_excel('/Users/weixin/Documents/2018高新申请/物联网表计采集收费系统/研发项目.xlsx')
#     print(df)
# except Exception as e:
#     print(e)


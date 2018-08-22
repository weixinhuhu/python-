import pandas as pd
import 高级.数据库.数据库连接 as MySql
import ssl
import  numpy as np

# 当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出该错误消息。

ssl._create_default_https_context = ssl._create_unverified_context

# 读取网络端csv文件
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

try:
    df = pd.read_csv(data_url)
    # print(df)
    # # 数据处理--------------------------------------------------
    # # 打印数据前五行
    # print(df.head())
    # # 打印数据后五行
    # print(df.tail())
    # # 选取第3行
    # print(df.iloc[3])
    # # 选取第2到第3行
    # print(df.iloc[2:4])
    # # 打印10~20行前三列数据
    # print(df.iloc[10:20,0:3])
    # # 提取不连续行和列的数据，这个例子提取的是第1,2,4行，第2,4列的数据
    # print(df.iloc[[1,2,4],[2,4]])
    # # 专门提取某一个数据，这个例子提取的是第三行，第二列数据（默认从0开始算哈）
    # print(df.iat[3, 2])
    # # 假设我们要筛选出小费大于$8的数据
    # print(df[df.tip>8])
    # # 数据筛选同样可以用”或“和”且“作为筛选条件
    # # #筛选出小费大于$7或总账单大于$50的数据
    # print(df[(df.tip > 7) | (df.total_bill > 50)])
    # # 筛选出小费大于$7且总账单大于$50的数据
    # print(df[(df.tip > 7) & (df.total_bill > 50)])
    # # 假如加入了筛选条件后，我们只关心day和time
    # print(df[['day', 'time']][(df.tip > 7) | (df.total_bill > 50)])

    # # 描述性统计-----------------------------------------------
    # print(df.describe())

    # #数据处理--------------------------------------------------
    # # 数据转置
    # print(df.T)
    # # 数据排序
    # print(df.sort_values(by='tip'))

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

# # 数据处理
# # 创建随机数框
# czf_data = pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))
# print(czf_data)
# #把第二列数据设置为缺失值
# czf_data.ix[2,:]=np.nan
# print(czf_data)
# #接着就可以利用插值法填补空缺值了
# print(czf_data.interpolate())

#按day这一列进行分组
group=df.groupby('day')
print(group.first())
print(group.last())

# 值替代
#首先创造一个Series
Series = pd.Series([0,1,2,3,4,5])
print(Series)
# 替换
print(Series.replace(0,10000000000000))
#列和列的替换同理
print(Series.replace([0,1,2,3,4,5],[11111,222222,3333333,44444,55555,666666]))
import pandas as pd
import ssl
# 当你urllib.urlopen一个 https 的时候会验证一次 SSL 证书 ，当目标使用的是自签名的证书时就会爆出该错误消息。
ssl._create_default_https_context = ssl._create_unverified_context
data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
try:
    df=pd.read_csv(data_url)
    print(df)
except Exception as e:
    print (e)
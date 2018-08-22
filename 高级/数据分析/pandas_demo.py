import pandas as pd

data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
try:
    df=pd.read_csv(data_url)
except Exception as e:
    print (e)
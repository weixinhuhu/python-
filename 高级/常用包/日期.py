from _datetime import datetime,timedelta
import time,timeit
#!/usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = 'weixin'
dt=datetime.now()
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)


# 表示一个时间间隔
t1=datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
td=timedelta(hours=22)
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))


# # timeit 时间测试和工具
# def p():
#     time.sleep(10.6)
# t1=time.time()
# p()
# print(time.time()-t1)

# 生成列表2种方法的比较

# c='''
# sum=[]
# for i in range(1000):
#     sum.append(i)
# '''
# 利用timeit调用代码
# t1=timeit.timeit(stmt="[i for i in range(1000)]",number=100000)

# t2=timeit.timeit(stmt=c,number=100000)
#
# print(t1)
#
# print(t2)


# timeit执行函数，测量执行时间
s='''
def doit(num):
    for i in range(num):
        print("Repeat fro {0}".format(i))
'''
# setup 负责把环境变量准备好
t=timeit.timeit("doit(num)",setup=s+"num=11",number=10)
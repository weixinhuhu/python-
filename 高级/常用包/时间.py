import time
#!/usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = 'weixin'

print(time.timezone)
print(time.altzone)
print(time.daylight)
# 时间戳
print(time.time())
# 系统时间
t=time.localtime()
print(str(t.tm_hour)+':'+str(t.tm_min))
# # 获取cpu时间 只支出3。3版本
# t=time.clock()
# # 延时
# for i in range(0,10):
#     print(i)
#     # time.sleep(1)
# t1=time.clock()
# print(t1-t)

# 2018 3。26 21：05
t=time.localtime()
ft=time.strftime("%Y年%m月%d日 %H时%M分")
print(ft)
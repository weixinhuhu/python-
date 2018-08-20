#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'weixin'
d={"one":1,"two":2,"three":3}
for k in d:
    print(k)

for k in d.keys():
    print(k,d[k])

for k in d.values():
    print(k)

dd={k:v for k,v in d.items() if v%2==1 }
print(dd)

i=d.items()
print(i)



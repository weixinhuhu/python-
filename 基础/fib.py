#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'weixin'
def fib(n):
    if n==1:
      return 1
    if n==2:
      return 1
    return fib(n-1)+fib(n-2)

for i in range(1,100):
    print(fib(i),end="\n")

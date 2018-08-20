#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'weixin'

class Student():
    def __init__(self,name="NoName",age="18"):
        self.name=name
        self.age=age
    def say(self):
        print("My name is {0},is {1}".format(self.name,self.age))
def sayHello():
        print("Hi,Hello Word")

if __name__=='_main_':
    print("My is Mod")
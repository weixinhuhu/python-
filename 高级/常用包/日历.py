#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'weixin'
import calendar
calendar.calendar(2018,l=0,c=0)
calendar.isleap(2020)
calendar.leapdays(2008,2022)
v,k=calendar.monthrange(2018,11)
print(v)
print(k)
m=calendar.monthcalendar(2018,12)
for ym in m:
    print(ym)
calendar.prmonth(2018,8)

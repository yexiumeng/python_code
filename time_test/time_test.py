#! /usr/bin/python
#_*_ coding: UTF-8 _*_

import time

ticks = time.time()
localtime = time.localtime() #默认值当前时间，可输入时间戳
asctime = time.asctime(localtime) 
strf_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

print "时间戳:",ticks
print "时间元组:",localtime
print "格式化时间:",asctime
print "格式化时间:",strf_time


import calendar

cal = calendar.month(2018,11)
print "2018-11"
print cal

print time.clock()

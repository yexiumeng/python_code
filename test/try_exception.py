#!/usr/bin/env  python
#_*_ coding=utf-8 _*_

try:
	print 1/0
except Exception,err:
	print "error msg is: %s" %(err)
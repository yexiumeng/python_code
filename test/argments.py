#!/usr/bin/env  python
#_*_ coding=utf-8 _*_

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-l',help="show full message",action="store_true")
parser.add_argument('-a',action="store_true")

#添加互斥组
group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",action="store_true")
group.add_argument("-q","--quiet",action="store_true")

args = parser.parse_args()

if args.l:
	print "yes"

if args.a:
	print "no"

#sys.argv 是所有参数组成的一个数组
print sys.argv[-1]
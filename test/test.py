#coding=utf-8

import os

if os.getuid() == 0:
	pass
else:
	print("不是root用户")
	sys.exit(1)

version = raw_input('请输入你想安装的python版本(2.7/3.5)')


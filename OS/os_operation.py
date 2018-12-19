#!/usr/bin/env python

import os

if os.access("./os_operation.py",os.F_OK):
	print("666")

res=os.system('pwd')


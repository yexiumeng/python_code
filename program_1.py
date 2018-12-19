#!/usr/bin/evn python
import argparse

parser = argparse.ArgumentParser(description="hello world")

parser.add_argument("--version","-v")
parser.add_argument("txt")

args = parser.parse_args()

txt = args.txt


print ("the output are %s" %(txt))

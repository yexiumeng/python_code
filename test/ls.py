#!/usr/bin/env  python
#_*_ coding=utf-8 _*_

#参数设置
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-l',action="store_true")
parser.add_argument('-a',action="store_true")
args = parser.parse_args()

#功能实现
import os
path = os.getcwd()
file_list = os.listdir(path)

def mode_print(perm_mode):
    mode_dict = {
        '0':'---',
        '1':'--x',
        '2':'-w-',
        '3':'-wx',
        '4':'r--',
        '5':'r-x',
        '6':'rw-',
        '7':'rwx'
    }
    return mode_dict[perm_mode]

def show_file_mes(target):
    full_path = path+"/"+target
    u_mode,g_mode,o_mode = str(oct(os.stat(full_path).st_mode)[-3:])

    u_mode_print = mode_print(u_mode)
    g_mode_print = mode_print(g_mode)
    o_mode_print = mode_print(o_mode)

    file_mes = u_mode_print+g_mode_print+g_mode_print
    return file_mes


def list_all_file(list_of_file=file_list):
    if args.a and args.l:
        for i in list_of_file:
            print show_file_mes(i),i
    elif args.l:
        for i in list_of_file:
            if i[0] != ".":
                print show_file_mes(i),i
    elif  args.a and args.l:
        for i in list_of_file:
            print show_file_mes(i),i
    else:
        for i in list_of_file:
            if i[0] != ".":
                print i,


if __name__ == "__main__":
    list_all_file()


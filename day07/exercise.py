#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise.py
"""
创建函数,在终端中打印矩形.
"""


def crete_tan(num):
    for row in range(num):
        if row == 0 or row == num - 1:
            print("*" * num)
        else:
            print("*%s*" % (" " * (num - 2)))


number = int(input("请输入整数："))
crete_tan(number)

#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise01.py
"""
在终端中输入整数
打印正数、 负数、零
"""

number = int(input("请输入一个整数："))
if number > 0:
    print("正数")
elif number == 0:
    print("零")
else:
    print("负数")

#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise08.py
"""
输入y继续，不输入y则退出
"""
while True:
    number = int(input("请输入数字："))
    if number > 0:
        print("正数")
    elif number < 0:
        print("负数")
    else:
        print("零")
    if input("请输入y继续，否则退出!") != "y":
        break

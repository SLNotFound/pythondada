#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise02.py
"""
在终端中获取一个整数，作为边长，打印矩形。
效果：
请输入整数:5
$$$$$
$   $
$   $
$   $
$$$$$
"""

num = int(input("请输入一个整数："))

for i in range(1, num + 1):
    if i == 1 or i == num:
        print("$" * num)
    else:
        print("$" + " " * (num - 2) + "$")

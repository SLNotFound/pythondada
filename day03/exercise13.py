#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise13.py
"""
在终端中输入任意整数，计算累加和.
"1234" -> "1" -> 累加 1
效果：
请输入一个整数:12345
累加和是 15
"""
num = input("请输入一个整数：")
result = 0
for item in num:
    result += int(item)
print("累加和是" + str(result))

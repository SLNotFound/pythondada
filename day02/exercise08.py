#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise08.py
"""
练习：在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""
num = int(input("请输入一个四位整数："))
result = num // 1000
result += num % 1000 // 100
result += num % 100 // 10
result += num % 10
print("结果是：" + str(result))

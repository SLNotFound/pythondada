#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise01.py
"""
根据下列文字，提取变量，使用字符串格式化打印信息
确诊67802人,治愈63326人,治愈率0.99
70秒是01分零10秒
"""

num1 = 67802
num2 = 63326
rate = 0.99
print("确诊%d人,治愈%d人,治愈率%.2f" % (num1, num2, rate))

print("%d秒是%.2d分零%d秒" % (70, 1, 10))

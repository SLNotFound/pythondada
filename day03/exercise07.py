#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise07.py
"""
判断一个年份是否为闰年
"""

year = int(input("请输入一个年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(str(year) + "年的2月有29天")
else:
    print(str(year) + "不是闰年")

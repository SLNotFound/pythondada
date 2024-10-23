#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise05.py
"""
在终端中输入月份，打印相应的天数.
1 3 5 7 8 10 12 有 31天
2 有 29天
4 6 9 11 有 30天
超过月份提示月份有误
效果：
请输入月份:10
31天
"""
month = int(input("请输入月份："))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31天")
elif month == 2:
    print("29天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
else:
    print("月份有误")

#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise16.py
"""
练习：累加10 -- 60之间，个位不是3/5/8的整数和。
"""

ret = 0
for i in range(10, 61):
    if i % 10 == 3 or i % 10 == 5 or i % 10 == 8:
        continue
    ret += i
print(ret)

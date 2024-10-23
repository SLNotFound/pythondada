#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise14.py
"""
练习：
在终端中累加 0 1 2 3
在终端中累加 2 3 4 5 6
"""
count1 = 0
for i in range(4):
    print(i)
    count1 += i
print(count1)

count2 = 0
for j in range(2, 7):
    print(j)
    count2 += j
print(count2)

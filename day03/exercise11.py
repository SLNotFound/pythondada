#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise11.py
"""
一张纸的厚度是0.01毫米
请计算，对折多少次超过珠穆朗玛峰(8844.43米)
思路:
数据：厚度、高度、次数
算法：厚度*=2 次数+=1
"""
thickness = 0.01
count = 1
while True:
    thickness *= 2
    if thickness > 8844430:
        break
    count += 1
print("对折" + str(count) + "次")

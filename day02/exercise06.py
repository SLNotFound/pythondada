#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise06.py
"""
练习2：古代的秤，一斤十六两。在终端中获取两，计算几斤零几两。
效果：
请输入总两数：100
结果为：6斤4两
"""
liang = int(input("请输入多少两："))
print("结果为：" + str(liang // 16) + "斤" + str(liang % 16) + "两")

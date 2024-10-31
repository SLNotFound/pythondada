#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise03.py
"""
定义函数,根据总两数,计算几斤零几两
"""


def count(number):
    jin = number // 16
    liang = number % 16
    return jin, liang


total_liang = int(input("请输入两："))
jin, liang = count(total_liang)
print(str(jin) + "斤零" + str(liang) + "两")

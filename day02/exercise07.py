#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise07.py
"""
匀变速直线运动的速度与位移公式：
位移 = 初速度 × 时间 + 加速度 * 时间的平方 / 2
已知(在终端中录入)：位移、时间、初速度
计算：加速度
效果：
请输入距离：100
请输入初速度：6
请输入时间：10
加速度是：0.8
"""

s = int(input("请输入距离："))
v = int(input("请输入初速度："))
t = int(input("请输入时间："))

g = (2 * (s - v * t)) / t ** 2
print("加速度是：" + str(g))

#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise04.py
"""
根据心理年龄与实际年龄，打印智商等级。
智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
天才：140以上（包含）
超常：120-139之间（包含）
聪慧：110-119之间（包含）
正常：90-109之间（包含）
迟钝：80-89之间（包含）
低能：80以下
"""

mental_age = int(input("请输入心理年龄："))
actual_age = int(input("请输入实际年龄："))

IQ = mental_age / actual_age * 100

if IQ < 80:
    print("低能")
elif IQ < 90:
    print("迟钝")
elif IQ < 110:
    print("正常")
elif IQ < 120:
    print("聪慧")
elif IQ < 140:
    print("超常")
else:
    print("天才")

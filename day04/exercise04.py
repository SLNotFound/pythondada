#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise04.py
"""
八大行星："水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星"
-- 创建列表存储4个行星：“水星” "金星" "火星" "木星"
-- 插入"地球"、追加"土星" "天王星" "海王星"
-- 打印距离太阳最近、最远的行星(第一个和最后一个元素)
-- 打印太阳到地球之间的行星(前两个行星)
-- 删除"海王星",删除第四个行星
-- 倒序打印所有行星(一行一个)
"""
planet_list = ["水星", "金星", "地球", "火星", "木星", "土星", "天王星", "海王星"]
four_planets_list = ["水星", "金星", "火星", "木星"]
print(four_planets_list)
four_planets_list.insert(2, "地球")
four_planets_list.append("土星")
four_planets_list.append("天王星")
four_planets_list.append("海王星")
print(four_planets_list)

print(four_planets_list[0])
print(four_planets_list[-1])

print(four_planets_list[0:2])

four_planets_list.remove("海王星")
del four_planets_list[4]
print(four_planets_list)

for item in four_planets_list[::-1]:
    print(item)

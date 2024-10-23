#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise05.py
"""
练习1：在终端中输入一个疫情确诊人数再录入一个治愈人数，打印治愈比例
格式：治愈比例为xx%
效果：
请输入确诊人数：500
请输入治愈人数：495
治愈比例为99.0%
"""

number_of_confirmed_cases = int(input("请输入疫情确诊人数："))
number_of_people_cured = int(input("请输入治愈人数："))

cure_rate = (number_of_people_cured / number_of_confirmed_cases) * 100
print("治愈比例为" + str(cure_rate) + "%")

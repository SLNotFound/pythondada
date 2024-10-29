#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise02.py
"""
将两个列表，合并为一个字典
姓名列表["张无忌","赵敏","周芷若"]
房间列表[101,102,103]
"""
test_dict = {}
name_list = ["张无忌", "赵敏", "周芷若"]
room_list = [101, 102, 103]
for i in range(len(name_list)):
    key = room_list[i]
    value = name_list[i]
    test_dict[key] = value

print(test_dict)

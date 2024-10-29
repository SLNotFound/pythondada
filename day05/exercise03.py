#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise03.py
"""
颠倒练习{101: '张无忌', 102: '赵敏', 103: '周芷若'}
{'张无忌': 101, '赵敏': 102, '周芷若': 103}
"""
test_dict = {}
name_list = ["张无忌", "赵敏", "周芷若"]
room_list = [101, 102, 103]
for i in range(len(name_list)):
    value = room_list[i]
    key = name_list[i]
    test_dict[key] = value

print(test_dict)
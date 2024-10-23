#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise09.py

"""
在终端中显示0 1 2 3
在终端中显示2 3 4 5 6
在终端中显示1 3 5 7
在终端中显示8 7 6 5 4
在终端中显示-1 -2 -3 -4 -5
"""

count1 = 0
while count1 < 4:
    print(count1)
    count1 += 1

count2 = 2
while count2 < 7:
    print(count2)
    count2 += 1

count3 = 1
while count3 < 8:
    print(count3)
    count3 += 2

count4 = 8
while count4 > 3:
    print(count4)
    count4 -= 1

count5 = -1
while count5 > -6:
    print(count5)
    count5 -= 1

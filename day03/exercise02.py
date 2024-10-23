#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise02.py
"""
在终端中输入课程阶段数,显示课程名称
效果：
输入： 输出：
1 Python语言核心编程
2 Python高级软件技术
3 Web 全栈
4 项目实战
5 数据分析、人工智能
"""

stage = int(input("请输入课程阶段数(1~5)："))
if stage == 1:
    print("1 Python语言核心编程")
elif stage == 2:
    print("2 Python高级软件技术")
elif stage == 3:
    print("3 Web 全栈")
elif stage == 4:
    print("4 项目实战")
else:
    print("5 数据分析、人工智能")
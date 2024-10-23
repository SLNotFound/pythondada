#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise12.py
"""
程序产生1个,1到100之间的随机数。
让玩家重复猜测,直到猜对为止。
每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
效果：
请输入要猜的数字:50
大了
请输入要猜的数字:25
小了
请输入要猜的数字:35
大了
请输入要猜的数字:30
小了
请输入要猜的数字:32
恭喜猜对啦,总共猜了5次
"""
import random

num = random.randint(1, 100)
count = 1
while True:
    guess = int(input("请输入您猜的数字："))
    if num > guess:
        print("小了")
        count += 1
    elif num < guess:
        print("大了")
        count += 1
    else:
        print("恭喜猜对啦,总共猜了" + str(count) + "次")

#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# ----------------------------
# ProjectName: pythondada
# Author: sunlei
# FileName: exercise15.py
"""
如果账号的密码错误3次，提示锁定账户
"""

for i in range(1, 4):
    account = input("请输入账号：")
    password = input("请输入密码：")
    if account == "test" and password == "123456":
        print("登录成功")
    else:
        print("登录失败")
        if 3 - i == 0:
            print("账户已锁定")
        else:
            print("你还剩余" + str(3 - i) + "次机会")

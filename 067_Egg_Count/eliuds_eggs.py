# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : eliuds_eggs.py
@Project            : 067_Egg_Count
@CreateTime         : 2026/8/16 23:11
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/8/16 23:11 
@Version            : 1.0
@Description        : None
"""


def egg_count(display_value):
    # bin() 方法
    binary = bin(display_value)[2:]

    # format() 方法 format(display_value, "b")

    count = str(binary).count('1')
    return count

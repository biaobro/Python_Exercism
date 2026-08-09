# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : line_up.py
@Project            : 065_Line_Up
@CreateTime         : 2026/8/9 21:33
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/8/9 21:33 
@Version            : 1.0
@Description        : None
"""


def line_up(name, number):
    dic = {1: "st", 2: "nd", 3: "rd"}
    if number > 999:
        print("please input ordinal number between 1-999!")
        return 0
    elif number > 99 and number % 100 not in (11, 12, 13):
        res = number % 100 % 10
    elif 100 > number > 9 and number not in (11, 12, 13):
        res = number % 10
    else:
        res = number

    # dic.get(key, "匹配不到key时的默认值")
    comb = str(number) + dic.get(res, "th")
    res = f"{name}, you are the {comb} customer we serve today. Thank you!"
    return res


# line_up("Mary", 112)

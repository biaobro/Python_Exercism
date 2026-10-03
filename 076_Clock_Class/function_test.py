# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : function_test.py
@Project            : 076_Clock_Class
@CreateTime         : 2026/10/3 20:46
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/10/3 20:46 
@Version            : 1.0
@Description        : None
"""


def calc(hour, minute):
    # 小时除法求余数， 分钟除法向下取整
    calc_hour = hour % 24 + minute // 60

    # 超过正整数 24，需要再求余数
    if calc_hour >= 24:
        calc_hour = calc_hour % 24

    # 超过负数 24，需要再求余数
    if calc_hour < -24:
        calc_hour = calc_hour % -24 + 24
        if calc_hour == 24: calc_hour = 0

    if -24 <= calc_hour < 0:
        calc_hour = calc_hour + 24

    calc_minute = minute % 60
    return f'{calc_hour:02d}:{calc_minute:02d}'


print(calc(22, 40))
print(calc(-2, 40))
print(calc(0, -1500))


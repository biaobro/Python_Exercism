# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : v2.py
@Project            : 069_Plane_Tickets_Generator
@CreateTime         : 2026/9/27 16:59
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/9/27 16:59 
@Version            : 1.0
@Description        : None
"""

from itertools import cycle, islice


def generate_seat_letters(number):
    yield from islice(cycle("ABCD"), number)

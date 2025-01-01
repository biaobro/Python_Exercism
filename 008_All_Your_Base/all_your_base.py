# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : all_your_base.py
@Project            : Python_008_All_Your_Base
@CreateTime         : 2023/2/12 18:45
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/12 18:45
@Version            : 1.0
@Description        : None
"""


def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    value = 0
    length = len(digits) - 1
    for index, digit in enumerate(digits):
        if digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        if digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        value += digit * pow(input_base, length - index)

    out_digits = []
    while True:
        if value // output_base != 0:
            out_digits.append(value % output_base)
            value = value // output_base
        else:
            out_digits.append(value % output_base)
            break
    return out_digits[::-1]


print(rebase(2, [1, -1, 1, 0, 1, 0], 10))

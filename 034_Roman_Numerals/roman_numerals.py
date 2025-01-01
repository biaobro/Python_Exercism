# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : roman_numerals.py
@Project            : Python_034_Roman_Numerals
@CreateTime         : 2023/2/19 22:24
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 22:24
@Version            : 1.0
@Description        : None
"""


def roman(number):
    Units = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    Tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    Hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    Thousands = ['M', 'MM', 'MMM']

    numerals = [Units] + [Tens] + [Hundreds] + [Thousands]
    # print(numerals)

    _str = str(number)
    print(_str)
    res = ''
    for i, num in enumerate(_str):
        if num == '0':
            continue
        res = res + numerals[len(_str)-1-i][int(num)-1]

    return res

print(roman(4))
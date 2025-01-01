# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : proverb.py
@Project            : Python_053_Proverb
@CreateTime         : 2023/2/24 18:29
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/24 18:29
@Version            : 1.0
@Description        : None
"""


def proverb(*input_data, qualifier=None):
    res = []
    if len(input_data) > 0:
        for i in range(len(input_data)-1):
            template = f"For want of a {input_data[i]} the {input_data[i+1]} was lost."
            res.append(template)
        if qualifier is not None:
            makeup = qualifier + ' ' + input_data[0]
        else:
            makeup = input_data[0]
        ending = f"And all for the want of a {makeup}."
        res.append(ending)
    print(res)
    return res
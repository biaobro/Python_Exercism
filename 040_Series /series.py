# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : series.py
@Project            : Python_040_Series
@CreateTime         : 2023/2/20 16:29
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 16:29
@Version            : 1.0
@Description        : None
"""


def slices(series, length):
    # if the slice length is zero.
    if length == 0:
        raise ValueError("slice length cannot be zero")

    # if the slice length is negative.
    if length < 0:
        raise ValueError("slice length cannot be negative")

    # if the series provided is empty.
    if len(series) == 0:
        raise ValueError("series cannot be empty")

    # if the slice length is longer than the series.
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    res = [series[i:i + length] for i in range(0, len(series) - length + 1)]
    return res

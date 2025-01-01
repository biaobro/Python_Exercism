# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : largest_series_product.py
@Project            : Python_061_Largest_Series_Product
@CreateTime         : 2023/3/3 23:26
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/3 23:26
@Version            : 1.0
@Description        : None
"""
from functools import reduce

import numpy


def largest_product(series, size):
    # any 全部为False 则返回 False
    # 只要有1个为 True，则返回 True
    if any(not char.isdigit() for char in series):
        raise ValueError("digits input must only contain digits")
    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if size == 0:
        return 1

    tbcs = [series[i:i + size] for i in range(0, len(series) - size + 1)]

    products = []
    for tbc in tbcs:
        if '0' in tbc:
            products.append(0)
        else:
            product = numpy.prod([int(char) for char in tbc], dtype='int64')
            # product = reduce((lambda x, y: int(x) * int(y)), tbc)
            products.append(product)
            print(tbc, product)
    print(products)
    return max(products)

# largest_product("1234a5", 2)
# largest_product("0123456789", 2)
# x= [23514624,1000]
# print(numpy.prod(x, dtype='int64'))
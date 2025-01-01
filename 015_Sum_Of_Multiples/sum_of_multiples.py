# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : sum_of_multiples.py
@Project            : Python_015_Sum_Of_Multiples
@CreateTime         : 2023/2/14 15:17
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/14 15:17
@Version            : 1.0
@Description        : None
"""


def sum_of_multiples(limit, multiples):
    factors = set()
    for multiple in multiples:
        if multiple > limit:
            continue
        for i in range(1, limit):
            if multiple * i >= limit:
                break
            factors.add(multiple * i)
    print(factors)
    return sum(factors)


print(sum_of_multiples(15, [4, 6]))

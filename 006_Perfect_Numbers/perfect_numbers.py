# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : perfect_numbers.py
@Project            : Python_006_Perfect_Numbers
@CreateTime         : 2023/2/12 17:26
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/12 17:26
@Version            : 1.0
@Description        : None
"""


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number <= 2:
        return 'deficient'

    res_factors = set()
    res_factors.add(1)
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            res_factors.add(i)
            res_factors.add(int(number / 2))
    print(res_factors)
    res_sum = sum(res_factors)
    if res_sum == number:
        return 'perfect'
    elif res_sum < number:
        return 'deficient'
    else:
        return 'abundant'
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : prime_factors.py
@Project            : Python_043_Prime_Factors
@CreateTime         : 2023/2/20 22:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 22:15
@Version            : 1.0
@Description        : None
"""
import time


def factors(startnum):
    start = time.time()
    prime_factors = []
    factor = 2  # Begin with a Divisor of 2
    while startnum > 1:
        if startnum % factor == 0:
            prime_factors.append(factor)
            startnum /= factor  # divide the startnum by the factor
        else:  # If the divisor is not a factor increase it by 1
            factor += 1
    print(time.time() - start)
    return prime_factors


def factors_b(value):
    start = time.time()
    # 第1个思路是，在[2, sqrt(n)] 的范围内遍历，看是否能被整除，如果可以则输出 i 以及 n / i
    # 第2个思路是 Vishwas Garg
    res = []

    # 先把2剔除，经过这步之后，value 一定是奇数
    # 并且不存在偶数的素因子，所以我们可以跳过所有偶数 (i += 2)
    while value % 2 == 0:
        res.append(2)
        value = value // 2

    for i in range(3, int(pow(value, 0.5)) + 1, 2):
        while value % i == 0:
            res.append(i)
            value = value // i

    if value > 2:
        res.append(value)
    print(time.time() - start)
    return res


# print(factors(500))
# print(factors_a(93819012551))
# print(factors_b(93819012551))

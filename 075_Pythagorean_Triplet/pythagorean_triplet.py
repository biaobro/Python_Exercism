# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : pythagorean_triplet.py
@Project            : 075_Pythagorean_Triplet
@CreateTime         : 2026/10/2 16:39
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/10/2 16:39 
@Version            : 1.0
@Description        : None
"""

def triplets_with_sum(number):
    res = []
    for a in range(1,int(number/3)):
        for b in range(a, number):
            c = number - a - b
            if a*a + b*b == c*c:
                res.append([a,b,c])

    return res

# triplets_with_sum(840)


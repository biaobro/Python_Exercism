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
    # 改为整数运算， // 表示向下取整
    # 因为 a < b < c，a + b + c = n，所以 a 不会到达 number 的 1/3
    for a in range(1, number//3 + 1):

        # 进一步缩小 b 的范围，因为 b < c, 且 c = n - a - b, 可以得到 b < (n-a)/2
        # 所以可以得到 b 的上下限
        for b in range(a+1, (number-a)//2+1):
            c = number - a - b
            if a*a + b*b == c*c:
                res.append([a,b,c])

    return res

# triplets_with_sum(840)


# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : square_root.py
@Project            : Python_064_Square_Root
@CreateTime         : 2023/3/5 9:49
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/5 9:49
@Version            : 1.0
@Description        : None
"""

# 二分法
def square_root(number):
    low, high, ans = 0, number, -1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= number:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)
    return ans

# 牛顿迭代法
def square_root_02(number):
    if number == 0:
        res = 0
    else:
        C, x0 = float(number), float(number)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        res = int(x0)
    print(res)

#
# square_root(10)
# square_root_02(10)

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : utils.py
@Project            : Python_023_Coin_Changes
@CreateTime         : 2023/2/19 10:03
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 10:03 
@Version            : 1.0
@Description        : None
"""

from functools import reduce


# 计算1个列表的所有元素乘积
# reduce(function, iterable[, initializer])
# 输入参数得是1个可迭代对象，列表，元组
def get_product(tbp):
    return reduce(lambda x, y: x * y, tbp)


xx = (1, 2, 3, 4)
print(get_product(xx))


# 在考量元素顺序的前提下
# 计算1个可迭代对象是否 为另1个可迭代对象的子集
def is_strict_subset(tbpa, tbpb):
    if len(tbpa) > len(tbpb):
        raise ValueError("The length of one must be less than the second.")

    # Highlight: 这个写法很赞，以一定窗口大小从1个可迭代对象中提取元素
    return any([tbpa == tbpb[i:i + len(tbpa)] for i in range(0, len(tbpb) - len(tbpa) + 1)])


tbpa = (2, 3, 5)
tbpb = (0, 1, 2, 3, 4, 5)
print(is_strict_subset(tbpa, tbpb))




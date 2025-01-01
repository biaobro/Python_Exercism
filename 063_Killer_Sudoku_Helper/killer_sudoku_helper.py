# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : killer_sudoku_helper.py
@Project            : Python_063_Killer_Sudoku_Helper
@CreateTime         : 2023/3/4 15:56
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/4 15:56
@Version            : 1.0
@Description        : None
"""
from itertools import combinations as comb


def combinations(target, size, exclude):
    input_list = [_ for _ in range(1, 10)]
    for e in exclude:
        del input_list[input_list.index(e)]
    out_list = []
    for c in comb(input_list, size):
        if sum(c) == target:
            out_list.append(list(c))
    print(out_list)
    return out_list

# combinations(45, 9, [])
# combinations(10, 2, [1, 4])

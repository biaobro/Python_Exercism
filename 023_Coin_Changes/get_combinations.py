# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : get_combinations.py
@Project            : Python_023_Coin_Changes
@CreateTime         : 2023/2/17 11:37
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/17 11:37 
@Version            : 1.0
@Description        : None
"""

from itertools import combinations

def combine(input_list, n):
    '''根据n获得列表中的所有可能组合（n个元素为一组）'''
    out_list = []
    for c in combinations(input_list, n):
        out_list.append(c)
    return out_list


def get_combinations(input_list):
    out_list = []
    for i in range(len(input_list)+1):
        temp_list = []
        for c in combinations(input_list, i):
            temp_list.append(c)
        out_list.extend(temp_list)
    return out_list

list1 = ['a', 'b', 'c', 'd']
list2 = [[1], [1, 2], [1, 2, 3, 4]]
print(get_combinations(list2))
    


# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : knapsack.py
@Project            : Python_059_Knapsack
@CreateTime         : 2023/3/3 11:38
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/3 11:38
@Version            : 1.0
@Description        : None
"""
import math
from itertools import combinations


def combine(input_list, n):
    '''根据n获得列表中的所有可能组合（n个元素为一组）'''
    out_list = []
    for c in combinations(input_list, n):
        out_list.append(c)
    return out_list


def get_combinations_efficient(input_list, limit, padding):
    out_list = []
    for i in range(1, len(input_list) + 1):
        temp_list = []
        for c in combinations(input_list, i):
            if sum([int(_[padding:]) for _ in c]) > limit:
                continue
            temp_list.append(c)
        out_list.extend(temp_list)
    return out_list


def maximum_value(maximum_weight, items):
    if len(items) == 0:
        return 0
    # 将字典列表简化
    l_matches = []
    for item in items:
        l_matches.append([_ for _ in item.values()])
    print(l_matches)

    # 只要有1个item 的weight小于maxim_weight, 就可以继续
    # 否则就是全部 item 的weight 都大于maxim_weight，就没有必要继续
    if any(match[0] > maximum_weight for match in l_matches):
        return 0

    # 转换成 集合 去重
    # s_matches = set()
    # for match in l_matches:
    #     s_matches.add(tuple(match))
    # print(s_matches)

    # 转换成字典，用出现顺序+weight 值作为键

    padding = math.ceil(len(l_matches)/10)
    # print('padding', padding)
    d_matches = {}
    for idx, match in enumerate(l_matches):
        d_matches.update({str(idx).ljust(padding, '0') + str(match[0]): match[1]})
    # print(d_matches)

    # 得到 weight 不超过limit 的组合
    groups = get_combinations_efficient(d_matches.keys(), maximum_weight, padding)
    # print('groups', groups)

    # 计算 value
    values = []
    for group in groups:
        _v = 0
        for idx in group:
            _v = _v + d_matches[idx]
        values.append(_v)
    # print(values)
    return max(values)


# items = [
#     {"weight": 5, "value": 10},
#     {"weight": 4, "value": 40},
#     {"weight": 6, "value": 30},
#     {"weight": 4, "value": 50},
# ]
# items = [
#                     {"weight": 70, "value": 135},
#                     {"weight": 73, "value": 139},
#                     {"weight": 77, "value": 149},
#                     {"weight": 80, "value": 150},
#                     {"weight": 82, "value": 156},
#                     {"weight": 87, "value": 163},
#                     {"weight": 90, "value": 173},
#                     {"weight": 94, "value": 184},
#                     {"weight": 98, "value": 192},
#                     {"weight": 106, "value": 201},
#                     {"weight": 110, "value": 210},
#                     {"weight": 113, "value": 214},
#                     {"weight": 115, "value": 221},
#                     {"weight": 118, "value": 229},
#                     {"weight": 120, "value": 240},
#                 ]
# print(maximum_value(750, items))
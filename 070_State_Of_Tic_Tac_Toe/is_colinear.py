# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : is_colinear.py
@Project            : 070_State_Of_Tic_Tac_Toe
@CreateTime         : 2026/9/28 10:01
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/9/28 10:01 
@Version            : 1.0
@Description        : None
"""


def is_colinear(points):
    """

    :param points: 列表，每个元素是(x,y)坐标
    :return: 3个点是否共线
    """
    if len(points) <= 2: return True

    (x1, y1), (x2, y2) = points[0], points[1]

    # 0 0; 3 5; 6 10
    for x, y in points[2]:
        if (y2 - y1) * (x - x1) != (x2 - x1) * (y - y1): return False
    return True

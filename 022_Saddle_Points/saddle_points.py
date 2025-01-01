# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : saddle_points.py
@Project            : Python_022_Saddle_Points
@CreateTime         : 2023/2/15 23:52
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/15 23:52
@Version            : 1.0
@Description        : None
"""


def saddle_points(matrix):
    if len(matrix) == 0:
        return matrix

    len_row = len(matrix[0])

    # 先扫描每行长度，如果存在不一致，则报错
    for row in matrix:
        if len(row) != len_row:
            raise ValueError("irregular matrix")

    # 定义1个空列表，用于存储待返回的结果
    res_dict = []

    # 先找到每行中的最大数，以及对应坐标
    # y 是行数纵坐标，x是每元素数量横坐标
    all_max_num_dict = {}
    row_max_num_dict = {}
    for y in range(len(matrix)):
        # 先假定第1个数为最大，保存它的坐标和数值
        max_num = matrix[y][0]
        row_max_num_dict.update({(y, 0): max_num})

        for x in range(1, len(matrix[y])):
            if matrix[y][x] < max_num:
                continue
            elif matrix[y][x] > max_num:
                max_num = matrix[y][x]
                # 如果发现更大的数值，清空已经进添加的
                row_max_num_dict.clear()
                row_max_num_dict.update({(y, x): matrix[y][x]})
            else:
                # 如果发现相等的，就在原有基础上追加
                row_max_num_dict.update({(y, x): matrix[y][x]})

        # 将行结果添加到全部结果中，然后清空row_max_num_dict，以便用于下一行
        all_max_num_dict.update(row_max_num_dict)
        row_max_num_dict.clear()

    # 然后遍历字典,将值取出 和同列中的数值比较
    for k, v in all_max_num_dict.items():
        # k 是个元组
        max_num_x, max_num_y = k
        match_flag = True
        for y in range(0, len(matrix)):
            if matrix[y][max_num_y] >= v:
                continue
            else:
                # matrix[max_num_x][y] < v: 说明这个数在列条件上不满足
                match_flag = False
                break

        # 到这里，说明这个数是该列中最小的，将它保存进最终的结果
        # 根据tests，输出形式是：[{"row": 2, "column": 1}]
        # row 和 col 都是从1开始数的，所以都加上1
        if match_flag:
            res_dict.append({"row": max_num_x+1, "column": max_num_y+1})

    # 返回结果
    return res_dict

# matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
# print(saddle_points(matrix))
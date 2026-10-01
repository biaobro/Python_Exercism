# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : game_of_life.py
@Project            : 071_Conway_Game_of_Life
@CreateTime         : 2026/9/30 18:51
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/9/30 18:51 
@Version            : 1.0
@Description        : https://exercism.org/tracks/python/exercises/game-of-life
"""


def tick(matrix):
    row = len(matrix)
    if row == 0: return []
    col = len(matrix[0])

    # 最多比较 8 个邻居，向右加，向下加 —— y轴方向与正常的坐标系是反的
    coords = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    # 这里需要特别注意，如果直接写 new_matrix = matrix 实际上是让两个变量指向同1个
    new_matrix = [row.copy() for row in matrix]

    for x in range(row):
        for y in range(col):
            live_count = 0

            for dx, dy in coords:
                new_x = x + dx
                new_y = y + dy

                # 去掉 try ... catch ... ，主动判断边界，而不是用异常做正常的边界判断
                if 0 <= new_x < row and 0 <= new_y < col:
                    if matrix[new_x][new_y] == 1:
                        live_count += 1

            # any live cell with two or three live neighbors lives on
            if matrix[x][y] == 1:
                # 只有2、3 符合情况
                if live_count < 2 or live_count > 3:
                    new_matrix[x][y] = 0

            # any dead cell with exactly three live neighbors becomes a live cell
            else:
                # 小于3、大于3时保持原状态
                # 等于3时变更为live
                if live_count == 3:
                    new_matrix[x][y] = 1

    return new_matrix


matrix = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
]
print(tick(matrix))

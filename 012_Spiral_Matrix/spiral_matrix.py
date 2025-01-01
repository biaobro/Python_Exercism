# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : spiral_matrix.py
@Project            : Python_012_Spiral_Matrix
@CreateTime         : 2023/2/13 16:25
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/13 16:25
@Version            : 1.0
@Description        : None
"""
RIGHT = 1
DOWN = 2
LEFT = 3
UP = 0


def spiral_matrix(size):
    # 00, 01, 02, 03
    # 10, 11, 12, 13
    # 20, 21, 22, 23
    # 30, 31, 32, 33
    # Highlight: 这种写法属于浅拷贝，内部的子列表指向的是同1个地址，不论修改哪个子列表，其他列表也会跟着变化，所以是有问题的
    # res = [[0] * size] * size
    if size == 1:
        return [[1]]

    towards = RIGHT

    # Highlight: 改用这种写法，每个子列表都是新创建的
    res = [[0 for _ in range(size)] for _ in range(size)]

    x_pos = y_pos = count = 0
    # 从0开始循环
    for idx in range(size*size):
        # 从1开始赋值
        res[x_pos][y_pos] = idx+1

        # count < 3 是固定的，3个边的规律固定
        # 前3个 都是按 size 转向
        if idx % (size - 1) == 0 and idx != 0 and count < 3:
            # 4 代表4个方向，固定值
            towards = (towards + 1) % 4
            count += 1

        if towards == RIGHT:
            y_pos += 1
        elif towards == DOWN:
            x_pos += 1
        elif towards == LEFT:
            y_pos -= 1
        elif towards == UP:
            x_pos -= 1

        # 如果下一个位置 不是0 ，需要转向，同时调整（回退）x_pos, y_pos
        if res[x_pos][y_pos] != 0:
            # 转向
            towards = (towards + 1) % 4

            # 前1个方向是 up，往回退是向下x要加
            if towards == RIGHT:
                y_pos += 1
                x_pos += 1
            # 前1个方向是 RIGHT
            elif towards == DOWN:
                x_pos += 1
                y_pos -= 1
            # 前1个方向是 DOWN
            elif towards == LEFT:
                x_pos -= 1
                y_pos -= 1
            # 前1个方向是 LEFT
            elif towards == UP:
                x_pos -= 1
                y_pos += 1

    return res


print(spiral_matrix(1))

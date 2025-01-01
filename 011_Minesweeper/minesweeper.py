# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : minesweeper.py
@Project            : Python_011_Minesweeper
@CreateTime         : 2023/2/13 11:02
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/13 11:02
@Version            : 1.0
@Description        : None
"""


def annotate(minefield):
    """
    :param minefield: type is list
    :return:
    """
    # Function body starts here
    # 第1步，拆解minefield，构建新的列表，[坐标，元素，本行长度]
    elements = {}
    length_flag = False
    for row_pos, inner_str in enumerate(minefield):
        if len(inner_str) == 0:
            continue
        for col_pos, char in enumerate(inner_str):
            length_flag = True
            if char not in [' ', '*']:
                raise ValueError("The board is invalid with current input.")
            else:
                # 考虑到每列的长度不一样？
                elements.update({str(row_pos) + str(col_pos): [char, len(inner_str)]})
    # 所有元素都为空
    if not length_flag:
        return minefield
    print(elements)

    # 需要特别注意的一点，上面得到的坐标，row_pos, col_pos
    # row 对应纵坐标 y
    # col 对应横坐标 x
    # 第2步，对字典进行处理
    res = minefield  # []
    row_count = len(minefield)
    col_count = len(minefield[0])
    for coordinate, element in elements.items():
        # 如果当前位置是 *，则直接跳过，开始新一轮迭代 如果是空格，才继续
        if element[0] == '*':
            continue
        if element[1] != col_count:
            raise ValueError("The board is invalid with current input.")

        # 重新拆解出 横纵坐标
        row_pos, col_pos = [int(num) for num in list(coordinate)]

        # 由于 range() 是左闭 右开，位置在边上的元素，要考虑其他方向缺失的问题
        # 1个方法就是判断坐标是否超限
        # 确定x，也就是左右移动的范围
        left = col_pos - 1
        right = col_pos + 1
        # 最左位置
        if col_pos == 0:
            left = 0
            # 只有1列
            if element[1] == 1:
                right = 0
        # 最右位置
        elif col_pos == (element[1] - 1):
            right = col_pos

        # 确定y，也就是上下移动的范围，从 up 到 down，up 是包含，down 是不包含
        up = row_pos - 1
        down = row_pos + 1
        # 最上面一行
        if row_pos == 0:
            up = 0
            # 只有1行
            if row_count == 1:
                down = 0
        # 最下面一行
        elif row_pos == (row_count-1):
            down = row_pos

        print('src', row_pos, col_pos)
        print('search range :', left, right, up, down) # 搜索范围
        star_count = 0

        # 把 y 也就是 row 放在外部， x 也就是 col 放在内部
        for y in range(up, down + 1):
            for x in range(left, right+1):
                print('target', x, y)
                if x == col_pos and y == row_pos:
                    continue
                elif elements[str(y) + str(x)][0] == '*':
                    star_count += 1
        print('star_count', star_count)

        # res 内部是字符串，不能直接赋值，先转换成列表操作，然后再还原成字符串
        if star_count > 0:
            row_content = list(res[row_pos])
            row_content[col_pos] = str(star_count)
            res[row_pos] = ''.join(row_content)
    return res


# print(annotate([" **", "***", "***"]))
# print(annotate(["   ", "   ", "   "]))
# print(annotate([]))
# print(annotate([" ", "*", " ", "*", " "]))
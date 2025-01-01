# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : matrix.py
@Project            : Python_027_Matrix
@CreateTime         : 2023/2/18 16:58
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/18 16:58
@Version            : 1.0
@Description        : None
"""


class Matrix:
    def __init__(self, matrix_string):
        _row_lst = []
        for row in matrix_string.split('\n'):
            _row = [int(char) for char in row.split(' ')]
            _row_lst.append(_row)
        self.rows = _row_lst
        print(self.rows)

        row_count = len(_row_lst)
        row_size = len(_row_lst[0])

        _col_list = []
        for x in range(row_size):
            _col = []
            for y in range(row_count):
                _col.append(_row_lst[y][x])
            _col_list.append(_col)
        self.cols = _col_list
        print(self.cols)

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.cols[index-1]

# matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
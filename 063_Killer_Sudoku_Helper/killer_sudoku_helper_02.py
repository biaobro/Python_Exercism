# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : killer_sudoku_helper_02.py
@Project            : Python_063_Killer_Sudoku_Helper
@CreateTime         : 2023/3/4 22:39
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/4 22:39
@Version            : 1.0
@Description        : None
"""

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_combinations(target, size, exclude):
    if target <= 0:
        return None
    if size == 1:
        if target <= 9 and target not in exclude:
            return target
        return None

    return [[digit, generate_combinations(target - digit, size - 1, [d for d in DIGITS if d in exclude or d <= digit])]
            for digit in DIGITS
            if digit not in exclude and digit < target / size]


def combinations(target, size, exclude):
    combos = generate_combinations(target, size, exclude)
    if isinstance(combos, int):
        flattened = [[combos]]
    else:
        while max([isinstance(combos[0][i], list) for i in range(len(combos[0]))]):
            new_combos = []
            for combo in combos:
                list_index = 0
                while isinstance(combo[list_index], int):
                    list_index += 1
                for nested_combo in combo[list_index]:
                    new_combos.append(combo[:list_index] + nested_combo)
            combos = new_combos
        flattened = combos
    return flattened


# combinations(10, 2, [1, 4])
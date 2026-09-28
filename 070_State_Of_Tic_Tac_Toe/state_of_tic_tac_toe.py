# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : state_of_tic_tac_toe.py
@Project            : 070_State_Of_Tic_Tac_Toe
@CreateTime         : 2026/9/27 17:15
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/9/27 17:15 
@Version            : 1.0
@Description        : None
"""


def gamestate(board):
    # 把字符串列表打散成1个1维大列表，每个元素用1个数字可以定位到
    elements = [col for row in board for col in row]
    # print(elements)

    # 统计 X 和 O 的数量
    x_count = elements.count('X')
    o_count = elements.count('O')
    # print(x_count, o_count)

    # 规则要求X 在先，所以如果数量关系不对，直接返回错误
    # Example when player O goes before player X.
    if x_count < o_count: raise ValueError("Wrong turn order: O started")

    # Example when player X goes twice.
    if x_count - o_count >= 2: raise ValueError("Wrong turn order: X went twice")

    # 赢的位置组合
    win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    winners = set()
    # 遍历所有组合，看是否存在满足条件的元素
    for a, b, c in win_lines:
        if elements[a] == elements[b] == elements[c] != ' ':
            winners.add(elements[a])

    # X 赢和 O赢 都算赢
    if winners:
        if len(winners) > 1:
            raise ValueError(
                "Impossible board: game should have ended after the game was won")
        else:
            return 'win'

    # 因为前面有过 if 判断， 所以到这里只剩下 x_count >= o_count 了，不需要再判断这个条件
    if ' ' in elements:
        return 'ongoing'

    return 'draw'

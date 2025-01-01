# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : scrabble_score.py
@Project            : Python_036_Scrabble_Score
@CreateTime         : 2023/2/19 23:31
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 23:31
@Version            : 1.0
@Description        : None
"""


def score(word):
    relations = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        'K': 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }

    word = word.upper()
    _lst = list(word)
    _set = set(_lst)
    _lst_ = list(_set)

    count = {}
    for char in _lst_:
        count.update({char: word.count(char)})

    res = 0
    for char, char_count in count.items():
        for k, v in relations.items():
            if char in k:
                res = res + char_count * v

    return res


print(score("a"))
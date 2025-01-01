# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : diamond.py
@Project            : Python_010_Diamond
@CreateTime         : 2023/2/12 23:34
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/12 23:34
@Version            : 1.0
@Description        : None
"""


def rows(letter):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    pos = alphabet.index(letter)
    tbps = [' '* pos + 'A' + ' '* pos]
    count = pos
    for i in range(1, pos + 1):
        count = count - 1
        tbp = ' ' * count + alphabet[i] + '*' * (i*2-1) + alphabet[i] + ' ' * count
        tbps.append(tbp)

    for i in range(pos + 1, pos * 2 + 1):
        tbps.append(tbps[pos * 2 - i])

    return tbps


print(rows('C'))

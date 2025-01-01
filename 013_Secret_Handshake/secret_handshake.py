# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : secret_handshake.py
@Project            : Python_013_Secret_Handshake
@CreateTime         : 2023/2/13 18:11
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/13 18:11
@Version            : 1.0
@Description        : None
"""


def commands(binary_str):
    code_dict = {
        0: 'wink',
        1: 'double blink',
        2: 'close your eyes',
        3: 'jump'
    }
    res = []
    b_list = list(binary_str)[::-1]
    for index, x in enumerate(b_list):
        if index == (len(b_list) - 1) and x == '1':
            res = res[::-1]
            break
        if x == '1':
            res.append(code_dict[index])
    return res


print(commands("10011"))

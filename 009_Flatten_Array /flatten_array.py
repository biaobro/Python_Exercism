# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : flatten_array.py
@Project            : Python_009_Flatten_Array
@CreateTime         : 2023/2/12 22:57
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/12 22:57
@Version            : 1.0
@Description        : None
"""


def flatten(iterable):
    if len(iterable) == 0:
        return iterable
    else:
        str_iterable = ','.join([str(i) for i in iterable])
        print(str_iterable)
        str_iterable = str_iterable.replace('None', '').replace('[', '').replace(']', '').replace(' ', '')
        print(str_iterable)
        res = []
        list_iterable = str_iterable.split(',')
        for char in list_iterable:
            if char == ',':
                continue
            if char == '':
                continue
            try:
                char = int(char)
            except Exception:
                pass
            finally:
                res.append(char)
        return res

# print(flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]))
# print(flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]))
# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : binary_search.py
@Project            : Python_046_Binary_Search
@CreateTime         : 2023/2/21 9:31
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/21 9:31
@Version            : 1.0
@Description        : None
"""


def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")

    search_list.sort()
    if value < search_list[0] or value > search_list[-1] :
        raise ValueError("value not in array")

    start, end = 0, len(search_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if value > search_list[mid]:
            start = mid + 1
        elif value < search_list[mid]:
            end = mid - 1
        else:
            return mid
    raise ValueError("value not in array")


# search_list = [1, 3, 4, 5, 6, 7, 8, 9]
# value = 4
# print(find(search_list, value))

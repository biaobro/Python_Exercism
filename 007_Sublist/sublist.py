# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : sublist.py
@Project            : Python_007_Sublist
@CreateTime         : 2023/2/12 18:26
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/12 18:26
@Version            : 1.0
@Description        : None
"""

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


# 这个 Exercise 的关键是要求顺序
def sublist(list_one, list_two):
    # A = [] and B = []
    if len(list_one) == len(list_two) == 0:
        return EQUAL
    # 　A = [] and B = [1, 2, 3]
    if len(list_one) == 0 and len(list_two) > 0:
        return SUBLIST
    # A = [1, 2, 3] and B = []
    if len(list_one) > 0 and len(list_two) == 0:
        return SUPERLIST

    # A = [1, 2, 3] and B = [1, 2, 3]
    # A = [1, 2, 3] and B = [1, 3, 2]
    if 0 < len(list_one) == len(list_two):
        for i in range(len(list_one)):
            if list_one[i] != list_two[i]:
                return UNEQUAL
        return EQUAL
    else:
        # A = [1, 2, 3] and B = [1, 2, 3, 4, 5]
        # A = [3, 4, 5] and B = [1, 2, 3, 4, 5]
        # A = [1, 2, 4] and B = [1, 2, 3, 4, 5]
        # A = [3, 4] and B = [1, 2, 3, 4, 5]
        str_one = ','.join([str(i) for i in list_one])
        str_two = ','.join([str(i) for i in list_two])
        print(str_one)
        print(str_two)
        if str_one in str_two:
            return SUBLIST
        elif str_two in str_one:
            return SUPERLIST
        else:
            return UNEQUAL

# print(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]))
# print(sublist([1, 0, 1], [10, 1]))
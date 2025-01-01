# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : acronym.py
@Project            : Python_031_Acronym
@CreateTime         : 2023/2/19 15:46
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 15:46
@Version            : 1.0
@Description        : None
"""


def abbreviate(words):
    words = words.replace('-', ' ').replace('_', ' ')

    word_list = words.split(' ')

    # Highlight : 去除空元素
    word_list = [x.strip() for x in word_list if x.strip()!='']

    res = ''
    for word in word_list:
        res = res + word.title()[0]
    return res

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : phone_number.py
@Project            : Python_041_Phone_Number
@CreateTime         : 2023/2/20 16:35
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 16:35
@Version            : 1.0
@Description        : None
"""
import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self.purify(number)
        self.area_code = self.number[:3]

    @staticmethod
    def purify(number):
        # 一步到位的方法，用正则表达式，大写表示非
        # 但根据tests，不能这么暴力...
        # regex = r"\D"

        # 把明显不符合要求的字符(+,(,), ,-,.)替换掉
        regex = r"\+|\(|\)| |-|\."
        num = re.sub(regex, '', number)

        regex_letter = '[a-zA-Z]'
        regex_punctuation = '@|:|!'
        num_len = len(num)

        if num_len > 11:
            raise ValueError("must not be greater than 11 digits")
        elif num_len < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif num_len == 11 and num[0] != '1':
            raise ValueError("11 digits must start with 1")
        elif num[-7] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif num[-7] == '1':
            raise ValueError("exchange code cannot start with one")
        elif num[-10] == '0':
            raise ValueError("area code cannot start with zero")
        elif num[-10] == '1':
            raise ValueError("area code cannot start with one")
        elif re.search(regex_punctuation, number) is not None:
            raise ValueError("punctuations not permitted")
        elif re.search(regex_letter, number) is not None:
            raise ValueError("letters not permitted")
        else:
            if num_len == 11 and num[0] == '1':
                num = num[1:]
            return num

    def pretty(self):
        return '(' + self.number[:3] + ')-' + self.number[3:6] + '-' + self.number[6:]

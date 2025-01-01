# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : luhn.py
@Project            : Python_025_Luhn
@CreateTime         : 2023/2/18 15:18
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/18 15:18
@Version            : 1.0
@Description        : None
"""


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # remove spaces
        self.card_num = self.card_num.replace(' ', '')

        # check length
        if len(self.card_num) <= 1:
            return False

        # check chars
        for char in self.card_num:
            if not char.isdigit():
                return False

        new_card_num = []
        card_len = len(self.card_num)
        for index in range(card_len - 1, -1, -1):
            num = int(self.card_num[index])
            # if card_len = 16, index start from 15
            # if card_len = 15, index start from 14
            if index % 2 == card_len % 2:
                new_num = num * 2 - 9 if num * 2 > 9 else num * 2
            else:
                new_num = num
            new_card_num.insert(0, new_num)
        if sum(new_card_num) % 10 == 0:
            return True
        return False

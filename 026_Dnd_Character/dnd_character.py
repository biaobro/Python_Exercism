# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : dnd_character.py
@Project            : Python_026_Dnd_Character
@CreateTime         : 2023/2/18 16:31
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/18 16:31
@Version            : 1.0
@Description        : None
"""
import secrets


class Character:
    def __init__(self):
        self.strength = self.generate_random_score()
        self.dexterity = self.generate_random_score()
        self.constitution = self.generate_random_score()
        self.intelligence = self.generate_random_score()
        self.wisdom = self.generate_random_score()
        self.charisma = self.generate_random_score()
        self.hitpoints = 10 + modifier(self.constitution)

    def generate_random_score(self):
        _lst = []
        for i in range(4):
            # 返回 [0, 7) 范围内的随机整数
            num = secrets.randbelow(7)
            if num == 0:
                num = num + 1
            _lst.append(num)

        min_num = min(_lst)
        del _lst[_lst.index(min_num)]
        score = sum(_lst)
        return score

    def ability(self):
        return self.generate_random_score()


def modifier(num):
    return (num - 10) // 2

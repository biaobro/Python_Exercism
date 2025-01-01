# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : robot_name.py
@Project            : Python_038_Robot_Name
@CreateTime         : 2023/2/20 15:11
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 15:11
@Version            : 1.0
@Description        : None
"""
import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate()
    def reset(self):
        previous_name = self.name
        while True:
            self.name = self.generate()
            if self.name != previous_name:
                break

    def generate(self):
        random_str = ''.join(random.choice(string.ascii_letters).upper() for _ in range(2))
        random_num = ''.join(random.choice(string.digits) for _ in range(3))
        return random_str + random_num


# r = Robot()
# print(r.name)


# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : robot_simulator.py
@Project            : Python_048_Robot_Simulator
@CreateTime         : 2023/2/21 19:23
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/21 19:23
@Version            : 1.0
@Description        : None
"""

# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 0


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, param):
        rec = self.param_retrieve(param)
        for k, v in rec.items():
            # k 是 1个字母 和 任意位数字的字符串组合
            if k[0] == 'L':
                self.direction = (self.direction + v) % 4
            elif k[0] == 'R':
                self.direction = (self.direction - v) % 4
            elif k[0] == 'A':
                coords_lst = list(self.coordinates)
                if self.direction == WEST:
                    coords_lst[0] = coords_lst[0] - v
                elif self.direction == SOUTH:
                    coords_lst[1] = coords_lst[1] - v
                elif self.direction == NORTH:
                    coords_lst[1] = coords_lst[1] + v
                else:
                    coords_lst[0] = coords_lst[0] + v

                self.coordinates = tuple(coords_lst)

    def param_retrieve(self, param):
        rec = {}
        count = 1
        # 第1个 for 循环，把 param 拆解成字典，键是 字符+出现位置（去重），值是 字符的次数
        # 以“LAAARRRALLLL”为例，得到的是{L1:1,A2:3,R3:3,A:1,L:4}
        for idx, char in enumerate(param):
            if idx == 0:
                rec.update({char + str(count): 1})
            else:
                # 如果当前字符 和 前一个字符相同，则 count 保持不变，但次数要变
                if char == param[idx - 1]:
                    rec.update({char + str(count): rec.get(char + str(count)) + 1})
                # 如果当前字符 和 前一个字符不同，count 加1，表示出现了不同字符，次数初始化为1
                else:
                    count = count + 1
                    rec.update({char + str(count): 1})
        print(rec)
        return rec

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : clock.py
@Project            : 076_Clock_Class
@CreateTime         : 2026/10/2 17:21
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/10/2 17:21 
@Version            : 1.0
@Description        : https://exercism.org/tracks/python/exercises/clock
"""


class Clock:
    def __init__(self, hour, minute):
        # __init__ 里保持原样，不做数据处理
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        # 小时除法求余数， 分钟除法向下取整
        calc_hour = self.hour % 24 + self.minute // 60

        # 超过正整数 24，需要再求余数
        if calc_hour >= 24:
            calc_hour = calc_hour % 24

        # 超过负数 24，需要再求余数
        if calc_hour < -24:
            calc_hour = calc_hour % -24 + 24
            if calc_hour == 24: calc_hour = 0

        if -24 <= calc_hour < 0:
            calc_hour = calc_hour + 24

        calc_minute = self.minute % 60
        return f'{calc_hour:02d}:{calc_minute:02d}'

    def __eq__(self, other):
        if self.__str__() == other.__str__():
            return True
        return False

    def __add__(self, minutes):
        self.minute = self.minute + minutes
        return self.__str__()

    def __sub__(self, minutes):
        self.minute = self.minute - minutes
        return self.__str__()


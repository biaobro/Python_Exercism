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
        # hour * 60 + minute 将输入时间统一转成分钟数， % 1440 让结果始终落在1天之内
        total_minutes = (self.hour * 60 + self.minute) % 1440

        # 取出小时
        hour = total_minutes // 60

        # 取出分钟
        minute = total_minutes % 60
        return f'{hour:02d}:{minute:02d}'

    def __eq__(self, other):
        # 处理other 不是 Clock的情况
        if not isinstance(other, Clock):
            return NotImplemented

        # 简化写法
        return str(self) == str(other)

    def __add__(self, minutes):
        # 不要直接修改原对象，也不要返回字符串
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)


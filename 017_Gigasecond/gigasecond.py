# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : gigasecond.py
@Project            : Python_017_Gigasecond
@CreateTime         : 2023/2/14 15:40
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/14 15:40
@Version            : 1.0
@Description        : None
"""
from datetime import datetime, timedelta


def add(moment):
    """
    :param moment: datetime(2011, 4, 25, 0, 0)
    :return: datetime(2043, 1, 1, 1, 46, 40)
    """
    delta = timedelta(seconds=1000000000)
    return moment + delta


print(add(datetime(2011, 4, 25, 0, 0)))



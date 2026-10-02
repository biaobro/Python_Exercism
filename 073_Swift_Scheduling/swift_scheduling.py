# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : swift_scheduling.py
@Project            : 073_Swift_Scheduling
@CreateTime         : 2026/10/2 09:38
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/10/2 09:38 
@Version            : 1.0
@Description        : https://exercism.org/tracks/python/exercises/swift-scheduling
时间值的处理方式
"""

import datetime
import calendar


def get_month_first_last_workday(year, month):
    # 该月第一天
    first_day = datetime.datetime(year, month, 1, 8, 0, 0)

    # 该月最后一天
    last_date = calendar.monthrange(year, month)[1]
    last_day = datetime.datetime(year, month, last_date, 8, 0, 0)

    # 如果第一天是星期六或星期日，往后移到星期一
    while first_day.weekday() >= 5:
        first_day += datetime.timedelta(days=1)

    # 如果最后一天是星期六或星期日，往前移到星期五
    while last_day.weekday() >= 5:
        last_day -= datetime.timedelta(days=1)

    return first_day, last_day


def delivery_date(start, description):
    # ext = "2012-02-14T09:00:00"

    # dt = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    dt = datetime.datetime.fromisoformat(start)
    weekday = dt.weekday()

    # print(dt)  # 2012-02-13 09:00:00
    # print(dt.year)  # 2012
    # print(dt.month)  # 2
    # print(dt.day)  # 13
    # print(dt.hour)  # 9
    # print(weekday)  # 0 表示 Monday

    if description == "NOW": return (dt + datetime.timedelta(hours=2)).isoformat()
    if description == "ASAP":
        if dt.hour < 13: return datetime.datetime(dt.year, dt.month, dt.day, 17).isoformat()
        return (datetime.datetime(dt.year, dt.month, dt.day, 13) + datetime.timedelta(
            days=1)).isoformat()
    if description == "EOW":
        if weekday in [0, 1, 2]:
            return (datetime.datetime(dt.year, dt.month, dt.day, 17) + datetime.timedelta(
                days=(4 - int(weekday)))).isoformat()
        if weekday in [3, 4]:
            return (datetime.datetime(dt.year, dt.month, dt.day, 20) + datetime.timedelta(
                days=(6 - int(weekday)))).isoformat()
        else:
            return None
    if description[-1] == 'M':
        month_target = int(description.replace('M', ''))
        if dt.month < month_target:
            first_workday = get_month_first_last_workday(dt.year, month_target)[0].isoformat()
        else:
            first_workday = get_month_first_last_workday(dt.year + 1, month_target)[0].isoformat()
        return first_workday
    if description[0] == 'Q':
        quarter_target = int(description.replace('Q', ''))
        month_target = quarter_target * 3
        quater_start = (dt.month - 1) // 3 + 1
        if quater_start <= quarter_target:
            last_workday = get_month_first_last_workday(dt.year, month_target)[1].isoformat()
        else:
            last_workday = get_month_first_last_workday(dt.year + 1, month_target)[1].isoformat()
        return last_workday

# delivery_date('', '')

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : resistor_color_expert.py
@Project            : 066_Resistor_Color_Expert
@CreateTime         : 2026/8/9 23:05
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/8/9 23:05 
@Version            : 1.0
@Description        : None
"""
import math


def resistor_label(colors):
    band_codes = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7,
                 "grey": 8, "white": 9}
    tolerance_codes = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%", "green": "0.5%", "brown": "1%", "red": "2%",
                      "gold": "5%", "silver": "10%"}

    if len(colors) == 1:
        res = "0 ohms"
        return res

    # 保留从开头到倒数第 2 个元素之前的所有元素
    value = ""
    for band in colors[:-2]:
        value = value + str(band_codes[band])

    band = band_codes[colors[-2]]
    value = int(value) * int(math.pow(10, band))

    if len(str(value)) > 6:
        unit = "mega"
        if value % 1000000 == 0:
            value = value // 1000000
        else:
            value = value / 1000000
    elif len(str(value)) > 3:
        unit = "kilo"
        if value % 1000 == 0:
            value = value // 1000
        else:
            value = value / 1000
    else:
        unit = ""

    tolerance = tolerance_codes[colors[-1]]

    res = f"{value} {unit}ohms ±{tolerance}"
    return res

# print(resistor_label(["orange", "orange", "black", "green"]))
# print(resistor_label(["blue", "grey", "brown", "violet"]))
# print(resistor_label(["blue", "grey", "white", "brown", "brown"]))
# print(resistor_label(["brown", "black", "red", "red"]))
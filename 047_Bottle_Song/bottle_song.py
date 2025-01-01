# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : bottle_song.py
@Project            : Python_047_Bottle_Song
@CreateTime         : 2023/2/21 12:51
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/21 12:51
@Version            : 1.0
@Description        : None
"""

units = ['No', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']


def recite(start, take=1):
    res = []
    for i in range(take):
        num_str = units[start - i]
        left_str = units[start - i - 1].lower()
        template = [
            f"{num_str} green {'bottles' if start - i != 1 else 'bottle'} hanging on the wall,",
            f"{num_str} green {'bottles' if start - i != 1 else 'bottle'} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {left_str} green {'bottles' if start - i - 1 != 1 else 'bottle'} hanging on the wall.",
        ]
        res.extend(template)
        res.append("")

    return res[:-1]


print(recite(10, take=2))




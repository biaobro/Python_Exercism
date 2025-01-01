# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : twelve_days.py
@Project            : Python_033_Twelve_Days
@CreateTime         : 2023/2/19 18:09
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 18:09
@Version            : 1.0
@Description        : None
"""


def recite(start_num, end_num):
    """

    :param start_verse: int
    :param end_verse: int
    :return: string
    """
    codes = {
        1: ["first", "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."],
        2: ["second", " two Turtle Doves, and"],
        3: ["third", " three French Hens,"],
        4: ["fourth", " four Calling Birds,"],
        5: ["fifth", " five Gold Rings,"],
        6: ["sixth", " six Geese-a-Laying,"],
        7: ["seventh", " seven Swans-a-Swimming,"],
        8: ["eighth", " eight Maids-a-Milking,"],
        9: ["ninth", " nine Ladies Dancing,"],
        10: ["tenth", " ten Lords-a-Leaping,"],
        11: ["eleventh", " eleven Pipers Piping,"],
        12: ["twelfth", " twelve Drummers Drumming,"],
    }

    res = []
    for n in range(start_num, end_num+1):
        _lst_tmp = codes[1][1].split(':')

        _str = ''
        if n > 1:
            for i in range(2, n+1):
                _lst_tmp.insert(1, codes[i][1])
            _lst_tmp[0] = _lst_tmp[0] + ":"
            _str = ''.join(_lst_tmp)

            _str = _str.replace('first', codes[n][0])
            res.append(_str)
        else:
            res.append(codes[1][1])

    return res

print(recite(3,3))


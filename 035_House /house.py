# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : house.py
@Project            : Python_035_House
@CreateTime         : 2023/2/19 22:59
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 22:59
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
        1: "This is the house that Jack built.",
        2: "the malt that lay in",
        3: "the rat that ate ",
        4: "the cat that killed ",
        5: "the dog that worried ",
        6: "the cow with the crumpled horn that tossed ",
        7: "the maiden all forlorn that milked ",
        8: "the man all tattered and torn that kissed ",
        9: "the priest all shaven and shorn that married ",
        10: "the rooster that crowed in the morn that woke ",
        11: "the farmer sowing his corn that kept ",
        12: "the horse and the hound and the horn that belonged to ",
    }

    res = []
    for n in range(start_num, end_num+1):
        _lst_tmp = codes.get(1).split('This is')

        _str = ''
        if n > 1:
            for i in range(2, n+1):
                _lst_tmp.insert(1, codes[i])
            _lst_tmp[0] = "This is " + _lst_tmp[0]
            _str = ''.join(_lst_tmp)

            res.append(_str)
        else:
            res.append(codes[1])

    return res

print(recite(1,4))




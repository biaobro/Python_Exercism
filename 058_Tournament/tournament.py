# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : tournament.py
@Project            : Python_058_Tournament
@CreateTime         : 2023/3/2 18:28
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/2 18:28
@Version            : 1.0
@Description        : None
"""


def tally(rows):
    res = []
    infos = {}
    for row in rows:
        *teams, result = row.split(';')
        for team in teams:
            if team in infos.keys():
                val = infos.get(team)
                val['mp'] = val['mp'] + 1
                if result == 'win':
                    val['w'] = val['w'] + 1
                    result = 'loss'
                elif result == 'draw':
                    val['d'] = val['d'] + 1
                else:
                    val['l'] = val['l'] + 1
                    result = 'win'
            else:
                if result == 'win':
                    infos.update({team: {'mp': 1, 'w': 1, 'd': 0, 'l': 0, 'p': 0}})
                    result = 'loss'
                elif result == 'draw':
                    infos.update({team: {'mp': 1, 'w': 0, 'd': 1, 'l': 0, 'p': 0}})
                else:
                    infos.update({team: {'mp': 1, 'w': 0, 'd': 0, 'l': 1, 'p': 0}})
                    result = 'win'
            infos[team]['p'] = infos[team]['w'] * 3 + infos[team]['d']

    # 输出要按照分数由高到低，队名首字母顺序
    for k, v in infos.items():
        # "Allegoric Alaskans             |  2 |  2 |  0 |  0 |  6",
        res.append(k.ljust(31, ' ') + "|" + " |".join([str(_).rjust(3, ' ') for _ in v.values()]))

    # 先按字母排序
    res.sort()
    print(res)

    # 然后按照 point 冒泡排序
    for i in range(len(res)):
        for j in range(len(res) - i - 1):
            if int(res[j][-3:].strip()) < int(res[j + 1][-3:].strip()):
                (res[j], res[j + 1]) = (res[j + 1], res[j])

    header = "Team                           | MP |  W |  D |  L |  P"
    res.insert(0, header)
    return res


# results = ["Allegoric Alaskans;Blithering Badgers;win"]
# results = [
#     "Devastating Donkeys;Blithering Badgers;win",
#     "Devastating Donkeys;Blithering Badgers;win",
#     "Devastating Donkeys;Blithering Badgers;win",
#     "Devastating Donkeys;Blithering Badgers;win",
#     "Blithering Badgers;Devastating Donkeys;win",
# ]
# print(tally(results))

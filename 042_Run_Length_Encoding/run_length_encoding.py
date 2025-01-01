# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : run_length_encoding.py
@Project            : Python_042_Run_Length_Encoding
@CreateTime         : 2023/2/20 20:58
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 20:58
@Version            : 1.0
@Description        : None
"""


def decode(string):
    res = ''
    d_count = 0
    # origin_string = string
    idx = -1
    while len(string):
        idx = idx + 1
        if idx == 0 and not string[idx].isdigit():
            res = res + string[idx]
            string = string[idx + 1:]
            idx = -1
        else:
            if string[idx].isdigit():
                d_count += 1
                continue
            else:
                num = eval(''.join(string[idx-d_count:idx]))
                res = res + string[idx] * num
                string = string[idx+1:]
                d_count = 0
                idx = -1

    return res


# print(decode("12WB12W3B24WB"))


def encode(string):
    rec = {}
    count = 1
    # 第1个 for 循环，把string拆解成字典，键是 字符+出现位置（去重），值是 字符的次数
    for idx, char in enumerate(string):
        if idx == 0:
            rec.update({char + str(count): 1})
        else:
            if char == string[idx - 1]:
                rec.update({char + str(count): rec.get(char + str(count)) + 1})
            else:
                count = count + 1
                rec.update({char + str(count): 1})
    print(rec)

    res = ''
    # 第2个 for 循环，把字典的键值对拼接
    for k, v in rec.items():
        pad = '' if v == 1 else str(v)
        res = res + pad + k[0]

    # 返回最终结果
    return res


# print(encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"))

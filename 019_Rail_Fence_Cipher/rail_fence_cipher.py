# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : rail_fence_cipher.py
@Project            : Python_019_Rail_Fence_Cipher
@CreateTime         : 2023/2/14 16:23
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/14 16:23 
@Version            : 1.0
@Description        : None
"""


def encode(message, rails):
    # 构造1个无关元素填充的列表，后期用有效内容替换
    lines = []
    for i in range(rails):
        lines.append(list('*' * len(message)))

    # y 从 -1 开始，因为要取 0，0
    y = -1
    turn_flag = False
    for index, char in enumerate(message):
        if turn_flag:
            y = y - 1
        else:
            y = y + 1
        lines[y][index] = char
        if index != 0 and y % (rails - 1) == 0:
            turn_flag = not turn_flag

    # 再把列表拼接回字符串
    decoded_msg = ''
    for line in lines:
        decoded_msg = decoded_msg + ''.join(line)
    return decoded_msg.replace('*', '')


# print(encode("WEAREDISCOVEREDFLEEATONCE", 3))
# print(encode("EXERCISES", 4))
# print(encode('XOXOXOXOXOXOXOXOXO',2))
# print(encode("THEDEVILISINTHEDETAILS",3))

def decode(encoded_msg, rails):
    lines = []
    len_e = len(encoded_msg)

    # 拆解 填充
    for rail in range(rails):
        line = '*' * rail
        turn_flag = True
        for index, char in enumerate(encoded_msg):
            # 首尾行的填充规律固定
            if rail == 0 or rail == rails-1:
                pads = (2 * rails - 3) * '*'
            else:
                if turn_flag:
                    pads = (2 * rails - 3 - 2 * rail) * '*'
                else:
                    pads = (1 + 2 * (rail - 1)) * '*'

                # 如果是中间行的话，每填充1次，间距就要变化
                turn_flag = not turn_flag
            # 拼接
            line = line + char + pads

            # 如果够数，或者超出，就截断，并退出本次循环
            if len(line) >= len_e:
                lines.append(line[:len_e])

                encoded_msg = encoded_msg[index+1:]
                break
    print(lines)

    res_str = ''
    turn_flag = False
    # y 从 -1 开始，因为要取 0，0
    y = -1
    for x in range(len_e):
        if turn_flag:
            y = y - 1
        else:
            y = y + 1
        res_str = res_str + lines[y][x]
        if x != 0 and y % (rails - 1) == 0:
            turn_flag = not turn_flag
    return res_str

# in:  TEITELHDVLSNHDTISEIIEA
# out: THEDEVILISINTHEDETAILS
# print(decode("TEITELHDVLSNHDTISEIIEA", 3))

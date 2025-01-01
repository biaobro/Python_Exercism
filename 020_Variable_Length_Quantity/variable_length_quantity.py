# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : variable_length_quantity.py
@Project            : Python_020_Variable_Length_Quantity
@CreateTime         : 2023/2/15 10:01
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/15 10:01
@Version            : 1.0
@Description        : None
"""


def encode(numbers):
    """
    :param numbers: 输入和输出都是形似 0xAA 的16进制数据，不是字符串
    :return:
    : 这里有个需要注意的地方是，Python 会将输入参数 0x40 (举例) 自动转换为 十进制的64
    : Python 不跟踪有关 base 的任何信息；无论在源代码中键入 0x1000 还是 4096，它都是相同的数字，并且 Python 以相同的方式存储它。
    : Python 打印数字时，必须选择一个基数，默认值总是十进制。如果要以不同的方式打印它，则需要指定不同的方式来执行字符串转换，例如 hex 函数
    """
    res = []
    for number in numbers:
        # 127 -> 0x7F
        if number <= 127:
            res.append(number)
            continue
        else:
            # 将数字转换成二进制 + 字符串格式，去掉开头的0b
            b_num_str = bin(number).replace('0b', '')
            b_num_len = len(b_num_str)
            print(b_num_str, b_num_len)
            # 如果二进制字符串恰好是14位，只需要处理2次
            # 大于14位，15，16时就需要处理3次
            loops = b_num_len // 7 + 1 if b_num_len % 7 != 0 else b_num_len // 7

            # 从前往后取，否则后面还得做一遍列表逆序处理
            for loop in range(0, loops):
                if loop == 0:
                    # 不足7位时，补 1 + 缺失的0
                    start = 0
                    end = b_num_len - 7 * (loops - 1)
                    pad = '1' + (7 - end) * '0'
                else:
                    start = b_num_len - 7 * (loops - loop)
                    end = start + 7 if start + 7 < b_num_len else b_num_len
                    pad = '0' if loop == loops - 1 else '1'
                print('start:end', start, end)
                new_str = '0b' + pad + b_num_str[start:end]

                # 将二进制字符串 直接转换为十进制数字
                new_num = eval(new_str)
                print(new_str, new_num)
                res.append(new_num)
    return res


# 解码的时候 就需要考虑多少bytes 对应1个整数的问题
def decode(bytes_):
    len_bytes = len(bytes_)
    if len_bytes == 1 and bytes_[0] <= 127:
        return bytes_

    # 如果只有1个byte，而且转换成二进制后，首位不是0，那这个入参就是非法的。和 encode 逻辑不符
    # encode 逻辑最后1个byte，首位是0
    if len_bytes == 1 and 128 <= bytes_[0] <= 255:
        raise ValueError("incomplete sequence")

    res = []
    num_str = '0b'
    for number in bytes_:
        # 将数字转换成二进制 + 字符串格式，去掉开头的0b
        # 不足8位的 补0，补够8位
        b_num_str_8b = bin(number).replace('0b', '').rjust(8, '0')

        # 截取后7位
        b_num_str_7b = bin(number).replace('0b', '').rjust(8, '0')[1:]
        print(b_num_str_7b)
        num_str = num_str + b_num_str_7b

        # 这里要做判断，如果某个字节转换成二进制后，第0个bit（从高往低），也就是从低往高的第8个bit，是0，表示这个字节是1个整数的末尾
        # 需要开启新统计
        if b_num_str_8b[0] == '0':
            res.append(eval(num_str))
            num_str = '0b'

    print(res)
    return res

# print(encode([0x80]))
# print(encode([0x2000]))
# print(encode([0x3FFF]))
# print(encode([0x40, 0x7F]))
# print(decode([0xC0, 0x0]))
# print(decode([0xFF, 0xFF, 0x7F]))
# print(decode([0x81, 0x80, 0x80, 0x0]))
# print(decode([0x8F, 0xFF, 0xFF, 0xFF, 0x7F]))
# print(decode( [ 0xC0, 0x0, 0xC8, 0xE8, 0x56, 0xFF, 0xFF, 0xFF, 0x7F, 0x0, 0xFF, 0x7F, 0x81, 0x80, 0x0, ] ))
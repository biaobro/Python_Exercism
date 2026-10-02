# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : crypto_square.py
@Project            : 072_Crypto_Square
@CreateTime         : 2026/10/1 17:59
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/10/1 17:59 
@Version            : 1.0
@Description        : https://exercism.org/tracks/python/exercises/crypto-square
"""
import math


def cipher_text(plain_text):
    # \W 表示「非单词字符」，而 Python 中的单词字符包含字母、数字和下划线 _。因此，如果输入中有下划线，它不会被删除。
    # result = re.sub('[\W]+', '', plain_text).lower()

    # 用 isalnum() 函数判断字符是否为字母或数字
    result = ''.join(char.lower() for char in plain_text if char.isalnum())
    length = len(result)

    # 如果长度为1 直接返回 不做处理
    if length == 1:
        return result

    # column 向上取整， row 向下取整
    column = math.ceil(math.sqrt(length))
    row = math.floor(math.sqrt(length))
    if row * column < length:
        row = column

    rectangle = []
    cipher_text = ''

    for i in range(row):
        rectangle.append(result[i * column:i * column + column].ljust(column))

    # print(rectangle_text)
    # 因为是按列读取，所以是 [j][i]
    for i in range(column):
        for j in range(row):
            cipher_text += rectangle[j][i]

        # 最后1行 不需要添加空格
        if i < column - 1:
            cipher_text += ' '

    return cipher_text


value = "Chill out."
print(cipher_text(value))

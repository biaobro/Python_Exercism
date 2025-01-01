# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : atbash_cipher.py
@Project            : Python_003_Atbash_Cipher
@CreateTime         : 2023/2/11 16:27
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/11 16:27 
@Version            : 1.0
@Description        : None
"""

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def encode(plain_text):
    ciphered_text = []
    char_count = 0
    for char in list(plain_text.lower()):
        # 是数字
        if char.isdigit():
            ciphered_text.append(char)
            char_count += 1
        # 不是数字，也不是字母
        elif not char.isalpha():
            continue
        # 字母
        else:
            ciphered_text.append(alphabet[25 - alphabet.index(char)])
            char_count += 1

        # 每隔5个补空格，
        if char_count % 5 == 0:
            ciphered_text.append(' ')

    # 有可能会在最后1个位置补上空格，用strip() 去掉
    return ''.join(ciphered_text).strip()


def decode(ciphered_text):
    ciphered_text = ''.join(ciphered_text.split(' '))
    plain_text = []
    for char in list(ciphered_text):
        if not char.isalpha():
            plain_text.append(char)
            continue
        plain_text.append(alphabet[25 - alphabet.index(char)])
    return ''.join(plain_text)

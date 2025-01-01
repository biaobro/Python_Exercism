# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : simple_cipher.py
@Project            : Python_044_Simple_Cipher
@CreateTime         : 2023/2/20 22:39
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 22:39
@Version            : 1.0
@Description        : None
"""
import secrets
import string


class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(100))
        self.key = key

    def encode(self, text):
        res = ''
        dict_k = self.key_retrieve()

        # key = 'abcdefghij'
        # plaintext = 'zzzzzzzzzz'
        # res = 'zabcdefghi'
        for idx, char_t in enumerate(text):
            pos_t = string.ascii_lowercase.index(char_t)
            new_pos = pos_t + dict_k.get(idx % len(dict_k))
            res = res + string.ascii_lowercase[new_pos % 26]
        return res

    def decode(self, text):
        res = ''
        dict_k = self.key_retrieve()

        # key = 'abcdefghij'
        # plaintext = 'zabcdefghi'
        # res = 'zzzzzzzzzz'
        for idx, char in enumerate(text):
            pos = string.ascii_lowercase.index(char)
            new_pos = pos - dict_k.get(idx % len(dict_k))
            res = res + string.ascii_lowercase[new_pos]
        return res

    def key_retrieve(self):
        dict_k = {}
        for idx, char in enumerate(self.key):
            pos = string.ascii_lowercase.index(char)
            dict_k.update({idx: pos})
        print(dict_k)
        return dict_k

x = Cipher('abcdefghij')
# y = x.encode('zzzzzzzzzz')
# print(y)

z = x.decode('zabcdefghi')
print(z)

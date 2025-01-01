# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : affine_cipher.py
@Project            : Python_056_Affine_Cipher
@CreateTime         : 2023/3/2 9:18
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/2 9:18
@Version            : 1.0
@Description        : None
"""
from string import ascii_lowercase

m = 26
group_size = 5


def get_prime_factors(value):
    # 第1个思路是，在[2, sqrt(n)] 的范围内遍历，看是否能被整除，如果可以则输出 i 以及 n / i
    # 第2个思路是 Vishwas Garg
    res = []

    # 先把2剔除，经过这步之后，value 一定是奇数
    # 并且不存在偶数的素因子，所以我们可以跳过所有偶数 (i += 2)
    while value % 2 == 0:
        res.append(2)
        value = value // 2

    for i in range(3, int(pow(value, 0.5)) + 1, 2):
        while value % i == 0:
            res.append(i)
            value = value // i

    if value > 2:
        res.append(value)
    return res


def coprime_check(a, m):
    # 第1步，找到a 和 m 中比较小的数字，得到其质数因子
    a, m = min(a, m), max(a, m)
    factors = get_prime_factors(a)
    # 第2步，遍历第1步的质数因子，看m是否能将其整除
    for factor in factors:
        if m % factor == 0:
            return False
    return True


def encode(plain_text, a, b):
    # a 和 m 要互为质数，即共同的因子只有1
    if not coprime_check(a, m):
        raise ValueError("a and m must be coprime.")
    res = ''
    count = 0
    for char in plain_text.lower():
        if char.isdigit():
            pad = char
            count = count + 1
        elif char.isalpha():
            i = ascii_lowercase.index(char)
            pad = ascii_lowercase[(a * i + b) % m]
            count = count + 1
        else:
            continue

        res = res + pad
        if count % 5 == 0:
            res = res + ' '
    return res.strip()


def get_mmi(a, m=26):
    if a > m and a % m != 1:
        return None
    for i in range(2, m):
        if a * i % m == 1:
            return i


def decode(ciphered_text, a, b):
    # a 和 m 要互为质数，即共同的因子只有1
    if not coprime_check(a, m):
        raise ValueError("a and m must be coprime.")
    mmi = get_mmi(a)
    res = ''
    for char in ciphered_text.lower():
        if char.isdigit():
            pad = char
        elif char.isalpha():
            pad = ascii_lowercase[mmi * (ascii_lowercase.index(char) - b) % m]
        else:
            continue

        res = res + pad
    return res

# print(get_mmi(19))
# print(encode('test', 5,7))
# print(decode('ybty',11,7))

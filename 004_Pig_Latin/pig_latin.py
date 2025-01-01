# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : pig_latin.py
@Project            : Python_004_Pig_Latin
@CreateTime         : 2023/2/11 18:54
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/11 18:54 
@Version            : 1.0
@Description        : None
"""


def translate_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'xr', 'yt']
    consonants = ['thr', 'sch', 'th', 'ch', 'rh', 'qu', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                  'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    # Rule 1
    for vowel in vowels:
        if word.startswith(vowel):
            return word + 'ay'

    # Rule 2,3,4
    for consonant in consonants:
        if word.startswith(consonant):
            word = word.replace(consonant, '')
            if word[:2] == 'qu':
                return word[2:] + consonant + 'qu' + 'ay'
            # elif word[0] == 'y':
            #     return word + consonant + 'ay'
            else:
                return word + consonant + 'ay'


def translate(text):
    words = text.strip().split(' ')
    res = ''
    for word in words:
        res_word = translate_word(word)
        res = res + res_word + ' '
    return res.strip()
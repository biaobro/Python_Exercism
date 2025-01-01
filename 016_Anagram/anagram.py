# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : anagram.py
@Project            : Python_016_Anagram
@CreateTime         : 2023/2/14 15:32
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/14 15:32
@Version            : 1.0
@Description        : None
"""


def find_anagrams(word, candidates):
    word_list = list(word.lower())
    word_list.sort()

    res = []
    for candi in candidates:
        if candi.lower() == word.lower():
            continue
        else:
            candi_list = list(candi.lower())
            candi_list.sort()
            if candi_list == word_list:
                res.append(candi)
    return res


candidates = ["Banana"]

print(find_anagrams("BANANA", candidates))

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : word_count.py
@Project            : Python_024_Word_Count
@CreateTime         : 2023/2/16 22:57
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/16 22:57
@Version            : 1.0
@Description        : None
"""


def count_words(sentence):
    sentence = sentence.lower().replace('\t', ' ').replace('\n', ' ').replace('"', ' '). \
        replace('!', ' ').replace(',', ' ').replace('.', ' ').replace(':', ' '). \
        replace('&', ' ').replace('@', ' ').replace('$', ' ').replace('%', ' '). \
        replace('^', ' ').replace('_', ' ').strip('\'')
    sentence = sentence.split(' ')
    print(sentence)
    new_sentence = []
    for word in sentence:
        if word == '':
            continue
        word = word.strip("\'")
        new_sentence.append(word)

    print(new_sentence)
    word_dict = {}
    for word in new_sentence:
        word_dict.update({word: new_sentence.count(word)})
    print(word_dict)
    return word_dict


# count_words(""""That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.""")
# count_words("car: carpet as java: javascript!!&@$%^&")
# count_words("'First: don't laugh. Then: don't cry. You're getting it.'")
count_words("hey,my_spacebar_is_broken")

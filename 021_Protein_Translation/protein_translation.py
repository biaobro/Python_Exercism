# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : protein_translation.py
@Project            : Python_021_Protein_Translation
@CreateTime         : 2023/2/15 19:09
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/15 19:09
@Version            : 1.0
@Description        : None
"""


def proteins(strand):
    translate_dict = {'AUG': 'Methionine',
                      ('UUU', 'UUC'): 'Phenylalanine',
                      ('UUA', 'UUG'): 'Leucine',
                      ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
                      ('UAU', 'UAC'): 'Tyrosine',
                      ('UGU', 'UGC'): 'Cysteine',
                      'UGG': 'Tryptophan',
                      ('UAA', 'UAG', 'UGA'): 'STOP'}

    res = []
    stop_flag = False
    for i in range(0, len(strand), 3):
        rna = strand[i:i + 3]
        for k in translate_dict.keys():
            if rna in k:
                if translate_dict[k] == 'STOP':
                    stop_flag = True
                    break
                else:
                    res.append(translate_dict[k])
                    break
        if stop_flag:
            break

    return res

value = "UAGUGG"
expected = ["Phenylalanine", "Phenylalanine"]
print(proteins(value))
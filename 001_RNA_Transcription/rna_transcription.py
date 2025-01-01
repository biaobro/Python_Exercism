# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : rna_transcription.py
@Project            : Python_001_RNA_Transcription
@CreateTime         : 2023/2/11 11:19
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/11 11:19 
@Version            : 1.0
@Description        : None
"""


def to_rna(dna_strand):
    rna_strand = dna_strand.replace('A', 'U').replace('T', 'A')
    rna_strand = list(rna_strand)
    for index, char in enumerate(rna_strand):
        if char == 'G':
            rna_strand[index] = 'C'
        elif char == 'C':
            rna_strand[index] = 'G'
    return ''.join(rna_strand)

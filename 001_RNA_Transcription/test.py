# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : test.py
@Project            : Python_001_RNA_Transcription
@CreateTime         : 2023/2/11 11:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/11 11:20 
@Version            : 1.0
@Description        : None
"""

import unittest
from rna_transcription import (
    to_rna,
)


# Tests adapted from `problem-specifications//canonical-data.json`
class RnaTranscriptionTest(unittest.TestCase):
    def test_empty_rna_sequence(self):
        self.assertEqual(to_rna(""), "")

    def test_rna_complement_of_cytosine_is_guanine(self):
        self.assertEqual(to_rna("C"), "G")

    def test_rna_complement_of_guanine_is_cytosine(self):
        self.assertEqual(to_rna("G"), "C")

    def test_rna_complement_of_thymine_is_adenine(self):
        self.assertEqual(to_rna("T"), "A")

    def test_rna_complement_of_adenine_is_uracil(self):
        self.assertEqual(to_rna("A"), "U")

    def test_rna_complement(self):
        self.assertEqual(to_rna("ACGTGGTCTTAA"), "UGCACCAGAAUU")


if __name__ == "__main__":
    unittest.main()

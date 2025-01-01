# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : high_scores.py
@Project            : Python_028_High_Scores
@CreateTime         : 2023/2/18 18:12
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/18 18:12
@Version            : 1.0
@Description        : None
"""
import copy


class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        # self.scores.sort() 会影响 self.scores 本身
        # list 比较特殊，直接赋值的话，和原来还是一样
        _scores = copy.deepcopy(self.scores)
        _scores.sort(reverse=True)

        return _scores[:3]

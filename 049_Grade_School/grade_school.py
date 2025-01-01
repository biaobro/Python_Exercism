# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : grade_school.py
@Project            : Python_049_Grade_School
@CreateTime         : 2023/2/22 18:35
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/22 18:35
@Version            : 1.0
@Description        : None
"""


class School:
    def __init__(self):
        self.book = dict()
        self.names = list()
        self.bools = list()

    def add_student(self, name, grade):
        if name in self.names:
            self.bools.append(False)
        else:
            self.names.append(name)
            _names = self.book.get(grade, [])
            _names.append(name)
            self.book.update({grade: _names})
            self.bools.append(True)
        print(self.book)

    def roster(self):
        print(self.book)
        res = []
        grades = [k for k in self.book.keys()]
        grades.sort()
        print('grades', grades)
        for grade in grades:
            v = self.book.get(grade)
            v.sort()
            res = res + v
        return res

    def grade(self, grade_number):
        _names = self.book.get(grade_number, [])
        _names.sort()
        return _names

    def added(self):
        return self.bools

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : kindergarten_garden.py
@Project            : Python_029_Kindergarten_Garden
@CreateTime         : 2023/2/19 13:42
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/19 13:42
@Version            : 1.0
@Description        : None
"""


class Garden:
    static_students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph',
                       'Kincaid', 'Larry']
    static_plants = ['Grass', 'Clover', 'Radishes', 'Violets']
    plant_codes = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }

    def __init__(self, diagram, students=None):
        if students is None:
            students = self.static_students

        # 得到的是1个2维数组
        self.diagram = diagram.split('\n')
        self.students = students
        self.students.sort()

    def plants(self, student):
        _ = []
        pos = self.students.index(student)
        codes = self.diagram[0][pos*2:pos*2+1+1] + self.diagram[1][pos*2:pos*2+1+1]
        for code in codes:
            _.append(self.plant_codes[code])
        return _

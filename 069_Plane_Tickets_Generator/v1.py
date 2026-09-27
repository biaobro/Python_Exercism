# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : v1.py
@Project            : 069_Plane_Tickets_Generator
@CreateTime         : 2026/9/27 16:58
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/9/27 16:58 
@Version            : 1.0
@Description        : None
"""


def generate_seat_letters(number):
    letters = "ABCD"

    for n in range(number):
        yield letters[n % 4]


def generate_seats(number):
    letters = generate_seat_letters(number)

    row = 1

    for n in range(number):
        yield f"{row}{next(letters)}"

        if (n + 1) % 4 == 0:
            row += 1

            if row == 13:
                row = 14

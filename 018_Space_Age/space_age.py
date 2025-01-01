# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : space_age.py
@Project            : Python_018_Space_Age
@CreateTime         : 2023/2/14 15:54
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/14 15:54
@Version            : 1.0
@Description        : None
"""


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.code = {
            'Mercury': 0.2408467,
            'Venus': 0.61519726,
            'Earth': 31557600,
            'Mars': 1.8808158,
            'Jupiter': 11.862615,
            'Saturn': 29.447498,
            'Uranus': 84.016846,
            'Neptune': 164.79132,
        }

    def on_earth(self):
        return round(self.seconds/self.code['Earth'],2)

    def on_mercury(self):
        return round(self.seconds/self.code['Earth']/self.code['Mercury'],2)

    def on_venus(self):
        return round(self.seconds/self.code['Earth']/self.code['Venus'],2)

    def on_mars(self):
        return round(self.seconds / self.code['Earth'] / self.code['Mars'], 2)

    def on_jupiter(self):
        return round(self.seconds / self.code['Earth'] / self.code['Jupiter'], 2)

    def on_saturn(self):
        return round(self.seconds / self.code['Earth'] / self.code['Saturn'], 2)

    def on_uranus(self):
        return round(self.seconds / self.code['Earth'] / self.code['Uranus'], 2)

    def on_neptune(self):
        return round(self.seconds / self.code['Earth'] / self.code['Neptune'], 2)


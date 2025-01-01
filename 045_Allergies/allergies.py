# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : allergies.py
@Project            : Python_045_Allergies
@CreateTime         : 2023/2/21 0:02
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/21 0:02
@Version            : 1.0
@Description        : None
"""


class Allergies:
    # 这个 sku 键值的和是 255，要能在给定任意数值的情况下，找到敏感物体的组合
    sku = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'
    }

    def __init__(self, score):
        self.score = score % 256

    def allergic_to(self, item):
        if item in self.lst:
            return True
        return False

    @property
    def lst(self):
        # 这里是根据 score 得到对应的sku，敏感物种类
        if self.score % 256 == 0:
            return []
        _lst = self.recursive_score([_ for _ in self.sku.keys()], self.score)
        print(_lst)
        return _lst

    # 首先借鉴二分法查找的思路，从 sku 的键值里，找到离 score 最近的那个数字，把数字减掉
    # 如果减掉后不为0，需要用到递归，继续寻找，直到差为0
    def recursive_score(self, items, key):
        pos = self.binary_search(items, key)
        res = [self.sku.get(items[pos[0]])]
        key = key - items[pos[0]]
        while key != 0:
            return res + self.recursive_score(items[:pos[0]], key)
        return res

    # 找到 score 的位置，返回是个元组
    # 如果 score 恰好等于某个数字，那元组只有1个元素，对应该数字的绝对坐标
    # 如果 score 不等于任何数字，那元组会有2个元素，对应该数字的坐标范围
    def binary_search(self, items, key):
        start, end = 0, len(items) - 1
        while start <= end:
            mid = (start + end) // 2
            if key > items[mid]:
                start = mid + 1
            elif key < items[mid]:
                end = mid - 1
            else:
                return mid,
        return end, start


# print(binary_search([1,2,4,8,16,32,64,128],7))
# print(binary_search([1,2,4,8,16,32,64,128],10))
# print(binary_search([1,2,4,8,16,32,64,128],3))
# print(binary_search([1,2,4,8,16,32,64,128],192))
# print(binary_search([1,2,4,8,16,32,64,128],128))
# print(sum([1,2,4,8,16,32,64,128]))
# print(Allergies(112).allergic_to("chocolate"))
# print(Allergies(509).lst)
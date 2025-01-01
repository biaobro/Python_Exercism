# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : zebra_puzzle.py
@Project            : Python_062_Zebra_Puzzle
@CreateTime         : 2023/3/4 9:45
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/4 9:45
@Version            : 1.0
@Description        : None
"""
infos = {
    1:'There are five houses',
    2:'The Englishman lives in the red house',
    3:'The Spaniard owns the dog',
    4:'Coffee is drunk in the green house',
    5:'The Ukrainian drinks tea',
    6:'The green house is immediately to the right of the ivory house',
    7:'The Old Gold smoker owns snails',
    8:'Kools are smoked in the yellow house',
    9:'Milk is drunk in the middle house',
    10:'The Norwegian lives in the first house',
    11:'The man who smokes Chesterfields lives in the house next to the man with the fox',
    12:'Kools are smoked in the house next to the house where the horse is kept',
    13:'The Lucky Strike smoker drinks orange juice',
    14:'The Japanese smokes Parliaments',
    15:'The Norwegian lives next to the blue house',
}

# next to 只是表示2个是挨着，不能说明方向
# 颜色可以首先确定下来, green 在 ivory 的右边，Norwegian 在第1个，同时挨着 Blue
# 然后可以确定 Norwegian 和 Englishman
# 然后是 Kools 和 horse
# 确定 Milk, Coffee
# 接下来需要按照假设进行尝试，先填入 13，同时提供 烟和饮料
# 根据3， 同时提供国籍 和 宠物，Spaniard 应该是在4或者5
# 根据5， 同时提供国籍 和 饮料，可以判断 Ukrainian 是在2 或者4
# 根据7， 11，同时提供 烟 和 宠物 信息，可以判断 应该在4 或者 5
# 根据13，同时提供烟和饮料，应该是在2或者4
# 根据14，同时提供国籍和烟，Japanese 应该是在2或者4，5

vars = [
    {'color': 'yellow',     'nation': 'Norwegian',  'smoke': 'Kools',           'drink': '',            'pet': ''},
    {'color': 'blue',       'nation': '',           'smoke': '',                'drink': '',            'pet': 'horse'},
    {'color': 'red',        'nation': 'Englishman', 'smoke': '',                'drink': 'Milk',        'pet': ''},
    {'color': 'ivory',      'nation': '',           'smoke': 'Lucky Strike',    'drink': 'orange juice', 'pet': ''},
    {'color': 'green',      'nation': 'Spaniard',   'smoke': '',                'drink': 'Coffee',      'pet': 'dog'}
]


from itertools import permutations
# Constraints
# 1. There are five houses.
# 2. The Englishman lives in the red house.
# 3. The Spaniard owns the dog.
# 4. Coffee is drunk in the green house.
# 5. The Ukrainian drinks tea.
# 6. The green house is immediately to the right of the ivory house.
# 7. The Old Gold smoker owns snails.
# 8. Kools are smoked in the yellow house.
# 9. Milk is drunk in the middle house.
# 10. The Norwegian lives in the first house.
# 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
# 12. Kools are smoked in the house next to the house where the horse is kept.
# 13. The Lucky Strike smoker drinks orange juice.
# 14. The Japanese smokes Parliaments.
# 15. The Norwegian lives next to the blue house.
#
# Each of the five houses is painted a different color, and their
# inhabitants are of different national extractions, own different pets,
# drink different beverages and smoke different brands of cigarets.
#
# Which of the residents drinks water?
# Who owns the zebra?
def next_to(x, y):
    """Is position x next to position y?"""
    return abs(x - y) == 1
def just_right_of(x, y):
    """Is x just right of y"""
    return x - y == 1
def owns_zebra():
    return solution()[1]
def drinks_water():
    return solution()[0]
def solution():
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))
    print(orderings)
    result = next([{Englishman: "Englishman", Spaniard: "Spaniard",
                    Ukranian: "Ukranian", Japanese: "Japanese",
                    Norwegian: "Norwegian"}[x] for x in (water, zebra)]
                  for (red, green, ivory, yellow, blue) in orderings
                  if just_right_of(green, ivory)
                  for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                  if Englishman is red
                  if Norwegian is first
                  if next_to(Norwegian, blue)
                  for (coffee, tea, milk, oj, water) in orderings
                  if coffee is green
                  if Ukranian is tea
                  if milk is middle
                  for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                  if Kools is yellow
                  if LuckyStrike is oj
                  if Japanese is Parliaments
                  for (dog, snails, fox, horse, zebra) in orderings
                  if Spaniard is dog
                  if OldGold is snails
                  if next_to(Chesterfields, fox)
                  if next_to(Kools, horse)
                  )
    print(result)
    return result

# solution()
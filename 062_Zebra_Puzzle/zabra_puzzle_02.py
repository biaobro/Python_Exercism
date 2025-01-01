# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : zabra_puzzle_02.py
@Project            : Python_062_Zebra_Puzzle
@CreateTime         : 2023/3/4 15:11
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/4 15:11
@Version            : 1.0
@Description        : None
"""

from typing import Dict, NamedTuple
from itertools import permutations, starmap

# rule 1
HOUSES = FIRST, _, MIDDLE, _, _ = range(5)


class UnsolveableError(Exception):
    """
    Error to raise if no solution is found.
    """


class Colors(NamedTuple):
    """
    Color of each house.
    """
    blue: int
    green: int
    ivory: int
    red: int
    yellow: int


class Persons(NamedTuple):
    """
    Person in each house.
    """
    englishman: int
    japanese: int
    norwegian: int
    spaniard: int
    ukrainian: int


class Drinks(NamedTuple):
    """
    Drink at each house.
    """
    coffee: int
    milk: int
    orange_juice: int
    tea: int
    water: int


class Smokes(NamedTuple):
    """
    Smoked at each house..
    """
    chesterfields: int
    kools: int
    lucky_strikes: int
    old_gold: int
    parliaments: int


class Pets(NamedTuple):
    """
    Pet at each house.
    """
    dog: int
    fox: int
    horse: int
    snails: int
    zebra: int


# pylint: disable=cell-var-from-loop
def solve() -> Dict[str, str]:
    """
    Solve the zebra problem.
    """
    orders = list(permutations(HOUSES))

    def _colors(color: "Colors") -> bool:
        # rule 6
        return color.ivory + 1 is color.green

    for colors in filter(_colors, starmap(Colors, orders)):
        def _persons(person: "Persons") -> bool:
            return (
                # rule 2
                    person.englishman is colors.red and
                    # rule 10
                    person.norwegian is FIRST and
                    # rule 15 (and 10)
                    person.norwegian + 1 is colors.blue
            )

        for persons in filter(_persons, starmap(Persons, orders)):
            def _drinks(drink: "Drinks") -> bool:
                return (
                    # rule 4
                        drink.coffee is colors.green and
                        # rule 5
                        drink.tea is persons.ukrainian and
                        # rule 9
                        drink.milk is MIDDLE
                )

            for drinks in filter(_drinks, starmap(Drinks, orders)):
                def _smokes(smoke: "Smokes") -> bool:
                    return (
                        # rule 8
                            smoke.kools is colors.yellow and
                            # rule 13
                            smoke.lucky_strikes is drinks.orange_juice and
                            # rule 14
                            smoke.parliaments is persons.japanese
                    )

                for smokes in filter(_smokes, starmap(Smokes, orders)):
                    def _pets(pet: "Pets") -> bool:
                        return (
                            # rule 3
                                pet.dog is persons.spaniard and
                                # rule 7
                                pet.snails is smokes.old_gold and
                                # rule 11
                                abs(pet.fox - smokes.chesterfields) == 1 and
                                # rule 12
                                abs(pet.horse - smokes.kools) == 1
                        )

                    for pets in filter(_pets, starmap(Pets, orders)):
                        # map the current permutation value to the printable string
                        key = {
                            persons.englishman: "Englishman",
                            persons.spaniard: "Spaniard",
                            persons.ukrainian: "Ukrainian",
                            persons.japanese: "Japanese",
                            persons.norwegian: "Norwegian",
                        }
                        # when we reach here we've got a solution
                        return {"water": key[drinks.water], "zebra": key[pets.zebra]}
    raise UnsolveableError("No solution found!")


def drinks_water() -> str:
    """
    Solve for who drinks water.
    """
    return solve()["water"]


def owns_zebra() -> str:
    """
    Solve for who owns the zebra.
    """
    return solve()["zebra"]

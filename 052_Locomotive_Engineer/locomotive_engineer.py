# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : locomotive_engineer.py
@Project            : Python_052_Locomotive_Engineer
@CreateTime         : 2023/2/24 11:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/24 11:20
@Version            : 1.0
@Description        : None
"""

"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*ids):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # res = []
    # for num in param:
    #     res.append(num)
    # return res

    # more advanced style
    return list(ids)


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # return [1] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]

    # more advanced style
    one, two, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, one, two]


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param stops: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # stops_list = []
    # for stop in stops.values():
    #     stops_list.append(stop)
    # route.update({'stops': stops_list})
    # return route

    # more advanced style
    return {**route, "stops": list(stops.values())}


# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    # zip(*可迭代对象)  得到的是 元组列表，内部是元组，外部是列表
    # 但这个测试要的是 列表列表，内部是列表，外部也是列表
    # *rest, = zip(*wagons_rows)
    # print(rest)
    # return [list(_) for _ in rest]

    # more advanced style
    return list(map(list, zip(*wagons_rows)))
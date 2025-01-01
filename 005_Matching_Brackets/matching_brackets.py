# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : matching_brackets.py
@Project            : Python_005_Matching_Brackets
@CreateTime         : 2023/2/11 22:40
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/11 22:40 
@Version            : 1.0
@Description        : None
"""


def is_paired(input_string):
    # 定义1个 嵌套字典
    bracket_dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    # 第1步，# 循环遍历字符串，得到每个 k,v 以及各自的位置，并以字典形式保存
    left_parts = {}
    right_parts = {}
    for index, char in enumerate(input_string):
        if char in bracket_dict.keys():
            # 得到 k 位置
            k_pos = input_string[index:].index(char)
            # 每找到1个 key，就存入字典。用于处理嵌套场景
            left_parts.update({k_pos + index: char})

        if char in bracket_dict.values():
            # 得到 v 位置
            v_pos = input_string[index:].index(char)
            # 每找到1个 val，就存入字典。用于处理嵌套场景
            right_parts.update({v_pos + index: char})

    print(left_parts)
    print(right_parts)
    # 判断 左半部分 和 右半部分 的数量是否一致，不一致也就没必要继续
    if len(left_parts) != len(right_parts):
        return False

    # 第2步，遍历2个字典，得到左半部分和右半部分的位置匹配对，
    match_parts = {}

    # left 部分要从 尾部开始，对 left_parts 按键大小 倒序排序
    # sorted() 是list 的方法，
    # 参数1待排序对象（隐式转换为list），
    # 参数2是排序参照，kv是left_parts 中的字典，kv[0] 就是字典的键
    # 参数3用于控制是正序 还是 倒序
    # 返回结果是list，所以需要再转换回 dict
    left_parts_reversed = dict(sorted(left_parts.items(), key=lambda kv: kv[0], reverse=True))

    for left_pos, left_part in left_parts_reversed.items():
        match_flag = False
        # right 部分要从 头部开始
        for right_pos, right_part in right_parts.items():
            # 跳过左侧部分，从左半部分所在位置的右侧开始遍历
            if right_pos < left_pos:
                continue
            # 如果找到匹配对象
            if right_part == bracket_dict[left_part]:
                match_flag = True
                # 将左半部分的位置，和右半部分的位置 作为键值对加入字典保存
                match_parts.update({left_pos: right_pos})
                # 一旦匹配成功，就剔除这个right_part，不再需要参与后续遍历
                del right_parts[right_pos]
                # 停止循环
                break
        # 如果 rights 遍历完一轮，没有找到 left_part 的匹配
        if not match_flag:
            return False

    # 第3步，处理第2步得到的 match_parts
    # match_parts 是键、值都是数字（位置）的字典
    # 为了便于访问 match_parts，将其转换成列表
    match_parts = list(match_parts.items())
    print(match_parts)

    #
    for index, outer_match_part in enumerate(match_parts):
        print(outer_match_part)
        # 场景：左半部分 出现在了右半部分的右边 -> ")()"
        if outer_match_part[0] > outer_match_part[1]:
            return False

        # 从match_parts 中剔除 outer_match_part
        inner_match_parts = match_parts[:index] + match_parts[index + 1:]

        # 将剩下的部分 逐一 和 outer_match_part 比较
        for inner_match_part in inner_match_parts:
            # 嵌套场景：(0,4) (1,5)
            if outer_match_part[0] < inner_match_part[0] < outer_match_part[1] < inner_match_part[1]:
                return False
    return True


# print(is_paired("{ }"))
# print(is_paired(")()"))
# print(is_paired("[]]"))
# print(is_paired("([{}({}[])])"))
# print(is_paired("{)()"))

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : say.py
@Project            : Python_037_Say
@CreateTime         : 2023/2/20 12:35
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 12:35
@Version            : 1.0
@Description        : None
"""
units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def group_retrieve(lst):
    # lst 是长度小于等于3的字符串数组
    # 开始倒序遍历
    res = _str = pad = ''
    for idx, char in enumerate(lst[::-1]):
        digit = int(char)
        if digit == 0:
            continue
        if idx == 1:
            # 如果倒数第2位 是0 或者 1
            if digit < 2:
                res = ''
                _str = units[eval(''.join(lst[-2:]))]
            else:
                _str = tens[digit - 2] + '-'
        else:
            if idx == 2:
                pad = ' hundred '
            _str = units[digit] + pad

        res = _str + res
    return res.strip('-').strip()


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    num_lst = list(str(number))
    print(num_lst)

    num_len = len(num_lst)

    # 数字只有1位的情况
    if num_len == 1:
        return units[number]
    # 数字小于3位
    elif 2 <= num_len <= 3:
        return group_retrieve(num_lst)
    # 数字大于3位
    else:
        # 先分组
        res = ''
        num_groups = []
        step = num_len % 3
        p_flag = False
        for i in range(num_len // 3):
            if step != 0 and not p_flag:
                num_groups.append(num_lst[0:num_len % 3])
                p_flag = True
            num_groups.append(num_lst[step + 3 * i:step + 2 + 3 * i + 1])

        group_len = len(num_groups)
        pads = ['', ' thousand ', ' million ', ' billion ']
        for i in range(group_len):
            if num_groups[i] == ['0', '0', '0']:
                continue
            group_index = group_len - i - 1
            group_str = group_retrieve(num_groups[i]) + pads[group_index]
            print(group_str)
            res = res + group_str
        return res.strip()


# print(say(987654321123))
print(say(14))


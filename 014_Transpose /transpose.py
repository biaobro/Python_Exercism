# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : transpose.py
@Project            : Python_014_Transpose
@CreateTime         : 2023/2/13 23:08
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/13 23:08
@Version            : 1.0
@Description        : None
"""


def transpose(lines):
    """
    :param lines: 输入类型是字符串
    :return:
    说明：大部分时候需求写得不清楚，只能根据给出的 tests 反推。比如这里的输入输出类型
    """
    if len(lines) == 0:
        return lines
    else:
        # 根据tests 反推，输入是个 字符串，将其转换为数组
        lines = lines.split('\n')
        if len(lines) == 1:
            return '\n'.join(list(lines[0]))

        len_list = []
        for line in lines:
            len_list.append(len(line))

        # 需要找到长度最长的那个元素
        # 用它的长度,来做内层控制
        max_len = max(len_list)
        max_len_pos = len_list.index(max_len)

        new_lines = []
        for y in range(0, max_len):
            new_line = []
            pad_needed = True
            # 因为需求是最长列的左边，元素为空时无条件补空格
            # 而在最长列的右边，要看后续是否有列是否比自己长，如果有，之间就还得补
            # 所以内部循环采用了倒序，这样方便判断右侧元素是否已经填充了值，
            # 如果成功填充，则标志位设置为 False，这样如果接下来同一行内发生 IndexError，就会进入到 标志位的判断
            for x in range(len(lines)-1, 0-1, -1):
                try:
                    # 顺序：[3,0],[2,0],[1,0],[0,0]
                    # 倒序：3 -> 2 -> 1 -> 0
                    char = lines[x][y]
                    new_line.append(char)
                    pad_needed = False
                except IndexError:
                    # 在最长列的左边，要无条件补
                    if x < max_len_pos:
                        new_line.append(' ')
                    # 在最长列的右边，要看情况是否补
                    # x > max_len_pos
                    else:
                        if not pad_needed:
                            new_line.append(' ')
                            pad_needed = True
            new_line.reverse()
            new_lines.append(''.join(new_line))
        return '\n'.join(new_lines)

# lines = ['ABC','DE']
# lines = ['AB','DEF']
# lines = ["11", "2", "3333", "444", "555555", "66666"]
# lines = ["The longest line.", "A long line.", "A longer line.", "A line."]
# param = '\n'.join(lines)
# new_lines = transpose(param)
# print(new_lines)
# for x in new_lines.split('\n'):
#     print(len(x))

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : wordy.py
@Project            : Python_002_Wordy
@CreateTime         : 2023/2/11 12:35
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/11 12:35 
@Version            : 1.0
@Description        : None
"""


def answer(question):
    operators = {
        'plus': '+',
        'minus': '-',
        'multiplied': '*',
        'divided': '/'}

    # 先将无关单词替换为空，并且移除头尾的空格，减少后期无效处理
    # 剩下的部分，用空格切割为列表
    # 这里得到的就已经是字符串列表，"What is 5?" -> ['5']
    # 注意by 前面多写1个空格
    word_list = question.replace('What is', '').replace(' by', '').replace('?', '').strip().split(' ')
    print(word_list)

    # 字符串替换为，然后转换为列表时，还是会留下 '' 占位
    # 这里用 '' 重新连接列表，以去掉 '' 占位
    # 这里处理 'What is?' 的场景
    if len(''.join(word_list)) == 0:
        raise ValueError("syntax error")

    # 经过字符串处理后，根据需求，能够处理的运算，至少会包含2个数字
    # 所以先根据数字数量进行分类处理

    # 判断整数的个数
    digit_count = 0
    for word in word_list:
        # 如果 int(word) 不是数字，会报错，所以这里用 try exception 来避开
        try:
            if type(int(word)) == int:
                digit_count += 1
        except Exception as e:
            continue

    # 没有数字
    if digit_count == 0:
        raise ValueError("unknown operation")
    # 1个数字，且没有其他任何单词 Iteration 0 — Numbers
    elif digit_count == 1 and len(word_list) == 1:
        return int(word_list[0])
    # 1个数字，但是剩余单词数量大于1 Unsupported operations ("What is 52 cubed?")
    elif digit_count == 1 and len(word_list) > 1:
        for operator in operators.keys():
            if operator in word_list:
                raise ValueError("syntax error")
        raise ValueError("unknown operation")
    else:
        # 至少2个数字，需要进一步判断运算符的情况
        # 运算符要对应2个数字，2个运算符要对应3个数字，不满足的继续剔除
        # Word problems with invalid syntax ("What is 1 plus plus 2?")
        # 判运算符的数量
        operator_count = 0
        for word in word_list:
            if word in operators.keys():
                operator_count += 1

        # 没有包含运算符
        if operator_count == 0:
            raise ValueError("syntax error")
        elif (digit_count - operator_count) != 1:
            raise ValueError("syntax error")
        else:
            # 到这里，运算符 和 数字 的数量都正确，可开始运算
            for index, word in enumerate(word_list):
                # 奇数位置的 word 应该是数字，偶数位的 word 应该是运算符，否则 raise error
                try:
                    # 如果 word 本身是字符，那这个 int() 转换就会引发异常
                    if type(int(word)) == int:
                        if index % 2 != 0:
                            raise ValueError("syntax error")
                except Exception:
                    if index % 2 != 1:
                        raise ValueError("syntax error")

                # 把数字也转换为 string，为后续的 eval() 函数做好准备
                word = str(word)
                if word in operators.keys():
                    # 将文本替换为真正的运算符，如 plus 替换为 +
                    word_list[word_list.index(word)] = operators[word]

            # 将处理后的列表再转换为字符串
            print(word_list)
            res_str = ''.join(word_list)
            print(res_str)

            # 需求是要求忽略运算符优先级，强制从左往右
            # 第一次运算是取3个元素
            res_str = ''.join(word_list[:3])
            res_int = eval(res_str)

            if len(word_list) > 3:

                # 后续的元素都是取2个元素
                for pos in range(3, len(word_list), 2):
                    res_str = str(res_int) + ''.join(word_list[pos:pos + 2])
                    res_int = eval(res_str)
            return res_int


print(answer("What is 1 plus 1?"))

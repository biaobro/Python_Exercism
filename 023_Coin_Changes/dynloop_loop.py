# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : dynloop_loop.py
@Project            : Python_023_Coin_Changes
@CreateTime         : 2023/2/17 14:08
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/17 14:08 
@Version            : 1.0
@Description        : None
"""

def dynloop_loop(data):
    # 变量初始化
    max_y_idx = len(data)  # 获取原2 维数组Y 轴最大值
    row_max_idx = 1  # 记录X 轴的最大值，初始为1，下面会计算
    arr_len, lst_row, lst_rst = [], [], []
    arr_idx = [0] * max_y_idx  # 保存每次提取max_y_idx 个元素的索引值的集合，初始值为[0, 0, 0, 0]

    # 将2 维数组data 转换成1 维数组lst_row
    for item in data:
        _n = len(item)  # 求原2 维数组中每一层的长度
        arr_len.append(_n)  # 保存原2 维数组中每一层的长度的集合
        lst_row += item  # 将原2 维数组的每个元素累加到1 维数组lst_row 中
        row_max_idx *= _n  # 记录1 维数组需要循环的总数

    # 遍历1 维数组
    for row_idx in range(row_max_idx):
        # 求每个被提取的元素的索引值
        for y_idx in range(max_y_idx):
            # 遍历原2 维数组各层长度的'切片'集合，例如：lst = [1, 2, 3, 4]
            # 则lst[2:] 为[3, 4] 即从下标2 开始后面全要；lst[:2] 为[1, 2] 即到下标2 之前都要
            # _pdt 是product 乘积的缩写，记录原2 维数组当前层之下所有层长度的乘积
            _pdt = 1
            for n in arr_len[y_idx+1:]:
                _pdt *= n
            # _offset 是偏移量，记录原2 维数组当前层之上所有层长度的和
            _offset = 0
            for n in arr_len[:y_idx]:
                _offset += n
            # 计算元素提取索引：当前X 轴的值除以_pdt，再与原2 维数组当前层长度取余，最后加上偏移量
            arr_idx[y_idx] = (row_idx // _pdt) % arr_len[y_idx] + _offset

        # 遍历索引集合，从1 维数组中提选元素放入_lst_tmp 中
        _lst_tmp = []
        for idx in arr_idx:
            _lst_tmp.append(lst_row[idx])
        # 最后将_lst_tmp 作为元素追加到lst_rst 中
        lst_rst.append(_lst_tmp)

    return lst_rst

data = [
        [1, 2],
        [3, 4, 5],
        [6, 7, 8, 9]
    ]
lst1 = dynloop_loop(data)
print(len(lst1))
print(lst1)
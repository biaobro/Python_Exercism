# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : dynloop_rcsn.py
@Project            : Python_023_Coin_Changes
@CreateTime         : 2023/2/17 14:48
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/17 14:48 
@Version            : 1.0
@Description        : None
"""

'''
递归法
从Y 轴第一层即index=0 开始从上往下递归，到了最底层就用一个循环每次将最底层的一个元素加入到要返回的list 中。
注意：Python 对递归层数是有限制的，而且不同操作系统的限制数不一样，在100 层以上就要考虑换个算法了。
'''
# data 数据源, cur_y_idx 当前Y 轴值, lst_rst 返回结果list, lst_tmp 用于临时拼装lst_rst 的元素
def dynloop_rcsn(data, cur_y_idx = 0, lst_rst = [], lst_tmp = []):
    max_y_idx = len(data) - 1  # 获取Y 轴最大索引值
    for x_idx in range(len(data[cur_y_idx])):  # 遍历当前层的X 轴
        lst_tmp.append(data[cur_y_idx][x_idx])  # 将当前层X 轴的元素追加到lst_tmp 中
        if cur_y_idx == max_y_idx:  # 如果当前层是最底层则将lst_tmp 作为元素追加到lst_rst 中
            lst_rst.append([*lst_tmp])
        else:  # 如果当前还不是最底层则Y 轴+1 继续往下递归，所以递归最大层数就是Y 轴的最大值
               # lst_rst 和lst_tmp 的地址也传到下次递归中，这样不论在哪一层中修改的都是同一个list 对象
            dynloop_rcsn(data, cur_y_idx+1, lst_rst, lst_tmp)
        lst_tmp.pop()  # 在本次循环最后，不管是递归回来的，还是最底层循环的，都要将lst_tmp 最后一个元素移除

    return lst_rst

# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : change.py
@Project            : Python_023_Coin_Changes
@CreateTime         : 2023/2/16 11:36
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/16 11:36 
@Version            : 1.0
@Description        : None
"""
from itertools import combinations


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    elif target == 0:
        return []

    # 最优方案里，肯定优选大数，所以先排序。 将coins从大到小排列
    coins.sort(reverse=True)

    # 如果最小的那个数，都比 target 大，那就没必要继续了
    if coins[-1] > target:
        raise ValueError("can't make target with given coins")

    """
    从这里往下其实是2个大的 for 循环
    第1个大 for 循环得到 coin 的组合
    第2个大 for 循环用于计算 coin 的组合是否能够凑成 target，换言之，求解n元1次方程
    如果target数字特别大，就可以考虑把2个 for 循环拆分，放到不同的线程中去跑，或者 map-reduce ?
    """

    # 第1个大 for 循环
    combinations_list = []
    for index, num in enumerate(coins):
        # 这个数字大于 target，跳过，要从小于等于target 的数字开始找
        if target < num:
            continue
        else:
            # 将前面大于 target的 num 过滤，只取符合要求的 coins 列表
            target_coins = coins[index:]
            print('target_coins', target_coins)

            # Todo:这里用到了 itertools 的1个库函数，也可以自己写，涉及到递归
            # 从1开始，跳过空元素组合，到len + 1 ：包含全部元素的组合结束
            # 这里得到的是所有可能的 coin 组合，单一 或 两两 或 三三，总数是 2的 n 次方
            # n 是 coin 数量，n个数可能产生的组合数量 2的n次方，先得到这些可能组合
            for i in range(1, len(target_coins) + 1):
                _lst_tmp = []
                # 内层循环控制每个组合的数量
                for c in combinations(target_coins, i):
                    _lst_tmp.append(c)
                # 注意这里 append 和extend 的组合，最后得到的是元组列表 [(20,), (10,), (5,), (2,), (20, 10), (20, 5), (20, 2), (10, 5),
                # (10, 2), (5, 2), (20, 10, 5), (20, 10, 2), (20, 5, 2), (10, 5, 2), (20, 10, 5, 2)]
                combinations_list.extend(_lst_tmp)
            print('combinations_list', combinations_list)

            # 只需要在target <= num 时跑1遍，跑完就退出 第1个大 for 循环
            break

    """
    接下来的过程是求解 n 元一次方程的过程，也就是针对每个组合，寻找对应因子，最终求和的过程
    这里颇费了一些时间，2天无法突破。最后借鉴到CSDN上【动态循环即不定层数循环】 的1个方案
    https://blog.csdn.net/yoshubom/article/details/104124333
    """
    # 第2个大 for 循环
    matched_combinations = set()
    solutions = []
    trailing_1_flag = False
    # 处理每个组合，判断是否能够完整替换 target
    for combination in combinations_list:
        # 举例 [10,5,1] 一定不是 target=15 的changes 方案，因为因子最小都是1
        if sum(combination) > target:
            continue

        # 提前把 长度为1 的 combination 处理掉，不进入后续的循环
        if len(combination) == 1:
            if target % combination[0] == 0:
                solutions.append([combination[0]] * (target // combination[0]))
            continue

        """
        因为 combination 的顺序是从短到长,然后从大到小，基于这个最重要的前提
        所以一旦包含大数字的 combination 符合要求,后面相同数量的 combination 就没有必要再比
        示例1: target=15, 已经找到 combination=(10,5), 那后面的(10,1) 和 (5,1) 就没有必要继续
        示例2: target=999, 已经找到 (100, 50, 20, 5, 2),那后面的 (100, 50, 20, 5, 1) 等等也就没有必要
        这里把被跳过的 combination 都打出来,做个对照
        """
        if len(combination) in matched_combinations:
            print('ignore', combination)
            continue

        # 把包含 1 的情况也提前处理掉，
        # 只需要处理1次 最大数 combination[0] 和 1 的组合，后面其他数字和 1 的combination 都跳过
        if combination[-1] == 1:
            if not trailing_1_flag:
                trailing_1_flag = True
                solutions.append([1] * (target % combination[0]) + [combination[0]] * (target//combination[0]))
            print('ignore', combination)
            continue

        """
        上面是把不符合要求的 combination 提前剔除
        下面是对 combination 正式求解的过程
        示例1：对于 target=999,combination = (100, 50, 20, 5, 2)
        得到的 factor_group = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1], [4, 3, 2, 1], [3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
        如果100 存在，那么50 能被100 整除，50就最多能出现1次
        相应地，20最多出现4次，5能被20整除，所以最多出现3次, 2 能被20整除，所以最多出现9次
        示例2：对于 target=27,combination=[5,4]
        得到的 factor_group = [[5,4,3,2,1],[6,5,4,3,2,1]]
        因为4 不能被5整除，所以4的范围还是要根据 target 来计算
        """
        factor = []
        factor_group = []
        for i, num in enumerate(combination):
            # combination 是个元组
            # 注意这里append的参数用了列表，最终 max_factors 的形式是1个嵌套列表，二维数组
            # 嵌套列表的形式便于后期控制循环
            # factor 内部全按从大到小排序，大的因子优先计算，如果不满足，小的就没必要计算了
            if i == 0:
                factor = [_ for _ in range(target // num, 0, -1)]
            else:
                # 如果这个数字是前面数字的因子，那数量要以前面这个数字为基准
                # 考虑 [10,5,2] 或者 [10,6,5,2] 的场景
                # 倒序遍历，先从最近的找，因为combination 本身是已经从大到小排好序的，距离最近，也意味着数值最近
                exact_div_flag = False
                for j in range(i-1, -1, -1):
                    if combination[j] % num == 0:
                        # 只要找到就停
                        factor = [_ for _ in range(combination[j] // num - 1, 0, -1)]
                        exact_div_flag = True
                        break
                # 如果在前面找不到他本身的倍数，就以 target 为基准
                # 考虑 target=27, combination=(5,4) 的场景
                if not exact_div_flag:
                    factor = [_ for _ in range(target // num, 0, -1)]

            factor_group.append(factor)

        # 例如：combination=(100, 50, 20, 5, 2)
        # factor_group = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1], [4, 3, 2, 1], [3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
        # 基于这个 combination 和 max_factors 开始寻找 change solution
        print('combination, factor_group', combination, factor_group)

        # 最大因子组合数量，用于控制最外层循环
        # [[9, 8, 7, 6, 5, 4, 3, 2, 1], [1], [4, 3, 2, 1], [3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1]]
        # 最坏的情况是循环 9*1*4*3*9 = 972 次
        row_max_idx = 1
        # 打扁成1个1维数组，并且统计每个列表的长度
        factor_combined = []
        # 保存每个子列表的长度，用于后期计算偏移量
        factor_len_arr = []

        for factor in factor_group:
            row_max_idx = len(factor) * row_max_idx
            factor_combined = factor_combined + factor
            factor_len_arr.append(len(factor))
        # print('factor_combined, factor_len_arr', factor_combined, factor_len_arr)

        # 定义1个保存偏移量的数组
        offset_idx = [0] * len(factor_len_arr)

        """
        下面开始遍历1 维数组
        这里最开始用的是 for 遍历，for row_idx in range(row_max_idx):
        但是for 循环没有办法跳数后继续，会导致一些无谓的没必要的循环
        改用 while 后，如果已经确认后续已经没有必要继续，就在循环体中直接调整变量
        最后这个方案去掉了跳数，while 需要手动 调整步进 + 1，for 不需要，还是改回for
        """
        # Highlight: 下面这个 for 循环是整段代码的 精华
        for row_idx in range(row_max_idx):
            # 求每个被提取的元素的索引值
            for y_idx in range(len(factor_group)):
                # _pdt 是product 乘积的缩写，记录原2 维数组当前层之下所有层长度的乘积，用于控制纵向偏移
                _pdt = 1
                for n in factor_len_arr[y_idx + 1:]:
                    _pdt *= n
                # _offset 是偏移量，记录原2 维数组当前层之上所有层长度的和
                _offset = 0
                for n in factor_len_arr[:y_idx]:
                    _offset += n
                # 计算元素提取索引：当前X 轴的值除以_pdt，再与原2 维数组当前层长度取余，最后加上偏移量
                offset_idx[y_idx] = (row_idx // _pdt) % factor_len_arr[y_idx] + _offset
            # print('arr_idx', arr_idx)

            # 遍历索引集合，从1 维数组中提选元素放入_lst_tmp 中
            _lst_tmp = []
            for idx in offset_idx:
                _lst_tmp.append(factor_combined[idx])
            # print('_lst_tmp', _lst_tmp)

            # 检验这个 combination 是否能满足要求
            # 举例: 对于target=21，combination 是 (5,2), _lst_tmp 是 [3,3] 时OK
            # 等同于2个数组，对应位置进行乘法运算，然后求和。 numpy 中应该有现成的方法可以做这个
            total = 0
            changes = []
            for pos, val in enumerate(_lst_tmp):
                total = combination[pos] * val + total
                changes = [combination[pos]] * val + changes
            if total == target:
                print('=' * 30 + 'get it' + '=' * 30)
                print(combination, _lst_tmp)
                solutions.append(changes)

                matched_combinations.add(len(combination))
                # 1个 combination 可能不止1组得到 target 的解法
                # 但因为都是从大往小找，只要找到就没必要继续了。 target = 999， coins=[100,50,20,5,2] 为例
                # 当找到 [9,1,2,1,2] 的解法时，即使后面还有 [9,1,1,1,12] 的解法，也没必要了
                # 如果是从小往大找的话，就得考虑跳数的问题
                break

    # 对得到的 changes 方案进行统一处理，找到长度最短的 solution
    if len(solutions) == 0:
        raise ValueError("can't make target with given coins")
    else:
        print('available solutions', solutions)
        min_len = len(solutions[0])
        best_solution = solutions[0]
        for solution in solutions:
            if len(solution) < min_len:
                min_len = len(solution)
                best_solution = solution
        return best_solution

# print(find_fewest_coins([10], 20))
# print(find_fewest_coins([1, 5, 10, 25], 1))
# print(find_fewest_coins([1, 5, 10, 25, 100], 15))
# print(find_fewest_coins([1, 4, 15, 20, 50], 23))
# print(find_fewest_coins([1, 5, 10, 21, 25], 63))
# print(find_fewest_coins([4, 5], 27))
# print(find_fewest_coins([2, 20], 21))
print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 999))
# print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 99))
# print(find_fewest_coins([2, 5, 10, 20, 50], 21))



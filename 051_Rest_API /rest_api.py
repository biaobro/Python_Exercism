# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : rest_api.py
@Project            : Python_051_Rest_API
@CreateTime         : 2023/2/24 0:20
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/24 0:20
@Version            : 1.0
@Description        : None
"""
import json


class RestAPI:
    def __init__(self, database=None):
        # the format of database is dictionary
        self.database = database

    def get(self, url, _payload=None):
        if url == '/users':
            # without Payload
            if _payload is None:
                res = self.database
            else:
                # within Payload
                payload = json.loads(_payload)
                res = {'users': []}
                users = self.database['users']
                # payload format is ?
                for query_user in payload['users']:
                    for exist_user in users:
                        if query_user == exist_user['name']:
                            res['users'].append(exist_user)
                            break
            # 统一返回
            return json.dumps(res)
        else:
            raise ValueError('operation not defined.')

    def post(self, url, _payload=None):
        # 输入参数 payload 是字符串形式，需要转换成字典
        payload = json.loads(_payload)
        if url == '/add':
            name = payload['user']
            # 初始化记录
            record = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database['users'].append(record)

            # 返回要求是字符串形式，需要把字典再转换成字符串
            print(self.database)
            return json.dumps(record)
        elif url == '/iou':
            # 拆解 payload
            lender_name = payload['lender']
            borrower_name = payload['borrower']
            amount = payload['amount']

            # 定义标志，因为要根据 name 寻找，需要遍历
            # 只需要处理 lender 和  borrower 2个人的信息就可以了，后面的就跳过
            lender_updated = borrower_updated = False

            for user in self.database['users']:
                # 处理 被借款人 信息
                if user['name'] == lender_name:
                    # 更新余额，借出去，表示有盈余，要加
                    user['balance'] = user['balance'] + amount

                    # 如果 借款人 已经是 我的欠款人，意味着 我是欠对方钱的，需要进一步判断
                    # 是更新 owes，还是 owed_by
                    if borrower_name in user['owes'].keys():
                        debt = user['owes'][borrower_name] - amount

                        # 借款 小于 欠款
                        if debt > 0:
                            user['owes'][borrower_name] = debt

                        # 借款 和 欠款 正好抵消
                        elif debt == 0:
                            user['owes'].pop(borrower_name)
                            print('the owes with ' + borrower_name + ' has been cleared.')

                        # 假如我欠对方3块，这次对方向我借钱4块，
                        # 意味着我会还清欠款，同时对方开始欠我1块
                        # 借款 大于 欠款，意味着欠款还清，同时对方开始欠我钱
                        # 这种情况下要同时更新 owes 和 owed_by
                        else:
                            user['owes'].pop(borrower_name)
                            user['owed_by'].update({borrower_name: abs(debt)})

                    # 如果 借款人
                    else:
                        # 更新 owed_by 字典，如果已经存在，就更新金额
                        # 如果不存在，就直接添加
                        if borrower_name in user['owed_by'].keys():
                            user['owed_by'][borrower_name] = user['owed_by'][borrower_name] + amount
                        else:
                            user['owed_by'].update({borrower_name: amount})

                    # 更新被借款人 处理完成 标志位
                    lender_updated = True

                # 处理借款人信息
                elif user['name'] == borrower_name:
                    # 更新余额，借回来，表示存在欠款，要减
                    user['balance'] = user['balance'] - amount

                    # 如果 被借款人 已经是我的欠款人，需要更新 owed_by，而不是 owes
                    if lender_name in user['owed_by'].keys():
                        debt = user['owed_by'][lender_name] - amount
                        if debt == 0:
                            user['owed_by'].pop(lender_name)
                            print('the owed_by with ' + lender_name + ' has been cleared.')
                        elif debt > 0:
                            user['owed_by'][lender_name] = debt
                        else:
                            user['owed_by'].pop(lender_name)
                            user['owes'].update({lender_name:abs(debt)})
                    else:
                        # 更新 owes 字典，如果已经存在，就更新金额
                        # 如果不存在，就直接添加
                        if lender_name in user['owes'].keys():
                            user['owes'][lender_name] = user['owes'][lender_name] + amount
                        else:
                            user['owes'].update({lender_name: amount})

                    # 更新 借款人 处理完成 标志位
                    borrower_updated = True

                # 如果 被借款人 和 借款人 都已经处理完成
                if lender_updated and borrower_updated:
                    break
            # get 函数的 payload 还是需要转换成字符串形式
            # 这里有个隐式的需求，也是根据tests反推出来，返回的结果中需要按照名字排序
            # get 1次只处理1个名字，所以在传参中把顺序调整好
            both = [lender_name, borrower_name]
            both.sort()
            return self.get('/users', json.dumps({"users": both}))
        else:
            raise ValueError('operation not defined.')


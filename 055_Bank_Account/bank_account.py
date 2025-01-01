# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : bank_account.py
@Project            : Python_055_Bank_Account
@CreateTime         : 2023/3/1 18:24
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/3/1 18:24
@Version            : 1.0
@Description        : None
"""
from threading import Lock


class BankAccount:
    def __init__(self):
        self.lock = Lock()
        self.balance = 0
        self.open_status = False

    def get_balance(self):
        with self.lock:
            if not self.open_status:
                raise ValueError("account not open")
            return self.balance

    def open(self):
        with self.lock:
            if self.open_status:
                raise ValueError("account already open")
            self.open_status = True

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        with self.lock:
            if not self.open_status:
                raise ValueError("account not open")
            self.balance = self.balance + amount

    def withdraw(self, amount):
        with self.lock:
            if not self.open_status:
                raise ValueError("account not open")
            if amount < 0:
                raise ValueError("amount must be greater than 0")
            if amount > self.balance:
                raise ValueError("amount must be less than balance")
            self.balance = self.balance - amount

    def close(self):
        with self.lock:
            if not self.open_status:
                raise ValueError("account not open")
            self.open_status = False
            self.balance = 0


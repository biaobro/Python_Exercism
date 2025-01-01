# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : nth_prime.py
@Project            : Python_039_Nth_Prime
@CreateTime         : 2023/2/20 15:40
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2023/2/20 15:40
@Version            : 1.0
@Description        : None
"""


def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = [2]
    count = 2
    for i in range(number-1):
        while True:
            is_prime = True
            count = count + 1
            up = int(pow(count, 0.5))
            for j in range(1, up+1):
                if count % j == 0 and j != 1:
                    is_prime = False
                    break
            if is_prime:
                primes.append(count)
                break

    print(primes)
    return primes[-1]


number = 6
print(prime(number))

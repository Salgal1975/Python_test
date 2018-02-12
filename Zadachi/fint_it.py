#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Учитывая массив, найдите int, который появляется нечетное число раз.
Всегда будет только одно целое число, которое появляется нечетным числом раз.
(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
'''


def find_it(seq):
    res = []
    a = []
    for i in range(len(seq)):
        res.append([seq.count(seq[i]), seq[i]])
    for i in res:
        if i[0] % 2 != 0:
            a.append(i[1])
    if len(a) != 1:
        a = a[0]
        # print(a)
        return a
    # print(type(a), a)


seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
find_it(seq)

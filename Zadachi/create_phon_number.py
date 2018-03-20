#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Напишите функцию, которая принимает массив из 10 целых чисел (от 0 до 9),
который возвращает строку этих чисел в виде номера телефона.
Пример:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# => returns "(123) 456-7890"
Возвращаемый формат должен быть правильным, чтобы завершить эту задачу.
Не забудьте пробел после закрывающей круглой скобки!
'''


def create_phone_number(n):
    len_n = len(n)
    # print(n)
    temp = ''
    for i in range(len_n):
        temp += str(n[i])
    # print(type(temp), temp)
    # print('(' + temp[0:3] + ') ' + temp[3:6] + '-' + temp[6:])
    return ('(' + temp[0:3] + ') ' + temp[3:6] + '-' + temp[6:])


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
create_phone_number(n)

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
У вас есть массив чисел. Ваша задача - сортировать восходящие нечетные числа, но даже номера должны быть на своих местах.
Ноль не является нечетным числом, и вам не нужно его перемещать. Если у вас пустой массив, вам нужно его вернуть.
пример:
sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''

def sort_array(source_array):
    new_array = []
    index = []
    new_array_2 = []
    index_2 = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            index.append(i)
            new_array.append(source_array[i])
        else:
            index_2.append(i)
            new_array_2.append(source_array[i])
    new_array = sorted(new_array)


source_array = [5, 3, 2, 8, 1, 4]
sort_array(source_array)

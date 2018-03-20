#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Возьмите 2 строки s1 и s2 в том числе только буквы от a до z. Верните новую
отсортированную строку, максимально возможную,0содержащую разные буквы, каждый
из которых принимается только один раз - от s1 или s2.
Примеры:
a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b)->"abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a)->"abcdefghijklmnopqrstuvwxyz"
'''


def longest(s1, s2):
    s = sorted(list(set(s1 + s2)))
    len_s = len(s)
    s1_new = ''
    for i in range(len_s):
        s1_new += s[i]
    return s1_new


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

longest(a, b)

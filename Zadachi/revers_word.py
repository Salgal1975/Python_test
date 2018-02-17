#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Завершите решение, чтобы оно меняло все слова внутри строки.
Пример:
reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
'''

def reverseWords(str_s:str):
    a = reversed(str_s.split())
    tmp = ''
    for i in a:
        tmp += i + ' '
    print(tmp)
    return tmp

g = "hello world!"
reverseWords(g)

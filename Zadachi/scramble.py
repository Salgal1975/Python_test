#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Запись function scramble( str1,str2 )возвращается, true если часть str1
символов может быть перегруппирована для соответствия str2, иначе возвращается
false.
Например:
str1 это 'cedewaraaossoqqyt' и str2 есть 'codewars' должен вернуться true.
str1 это 'rkqodlw'и str2 есть 'world' выход должен вернуться true.
str1 это ' katas' и str2 'steak' должен вернуться false.
Будут использоваться только строчные буквы (az). Никакие знаки препинания или
цифры не будут включены. Необходимо учитывать производительность
'''


def scramble(s1, s2):
    temp = 0
    if s1 != s2:
        # print(len(s2), temp)
        for s in s2:
            a = s in s1
            # print(a, s)
            if a:
                temp += 1
            if (temp == len(s2)):
                print(len(s2), temp)
                return True
            # print('True')
        print(len(s2), temp)
        # else:
        #     return False
    #     print('False')
    return False


s1 = 'katas'
s2 = 'steak'

res = scramble(s1, s2)
print(res)

'''
def scramble(s1, s2):
    if s1 == s2:
        return True
    else:
        temp = 0
        for s in s2:
            a = s in s1
            if a:
                temp += 1
        if (temp == len(s2)):
            return True
        else:
            return False
'''

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def encrypt(text, n):
    if n == 0:
        return text
    elif text == '':
        text = ''
        return text
    elif text is None:
        text = None
        return text
    while n > 0:
        new_text = ""
        new_text_2 = ""
        for i in range(1, len(text), 2):
            new_text += text[i]
        for i in range(0, len(text), 2):
            new_text_2 += text[i]
        text = new_text + new_text_2
        n -= 1
    # print(text)
    return text


def decrypt(encrypted_text, n):
    if n == 0:
        return encrypted_text
    elif encrypted_text == '':
        encrypted_text = ''
        return encrypted_text
    elif encrypted_text is None:
        encrypted_text = None
        return encrypted_text
    while n > 0:
        new_text = ""
        new_text_2 = ""
        for i in range(1, len(encrypted_text), 2):
            new_text_2 += encrypted_text[i]
        for i in range(0, len(encrypted_text), 2):
            new_text += encrypted_text[i]
        encrypted_text = new_text_2 + new_text
        n -= 1
    # print(encrypted_text)
    return encrypted_text


a = "This kata is very!"
b = encrypt(a, 1)
c = decrypt(b, 1)
print(b, '****', c)

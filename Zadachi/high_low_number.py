#!/usr/bin/env python3
'''
high_and_low("1 2 3 4 5")   # return "5 1"
high_and_low("1 2 -3 4 5")  # return "5 -3"
high_and_low("1 9 3 4 -5")  # return "9 -5"
'''


def high_and_low(number):
    # number = number.replace("", "")
    # print(type(number), number)
    # print('*************1**************')
    a = ' '.join(number.split())
    a = a.split()
    # print('*************2**************')
    # print(type(a), a)
    # print('*************3**************')

    a = [c for c in a]
    # print('*************4**************')
    for k in range(0, len(a)):
        a[k] = int(a[k])
    # print('************5***************')
    # print(type(a), a)
    # print('************6***************')

    x = max(a)
    y = min(a)

    return x, y


# high_and_low("1 9 3 4 -5 100")

# '''
def test_min_max():
    print('*************************')
    x1 = high_and_low("1 2 3 4 5 -100 1000")
    print(x1)
    if x1 == (1000, -100):
        print('test1-OK: ', x1)
    else:
        print('test1-FAILD: ', x1)
    print('*************************')
    x2 = high_and_low("1 2 -3 4 5")
    print(x2)
    if x2 == (5, -3):
        print('test2-OK: ', x2)
    else:
        print('test2-FAILD: ', x2)
    print('*************************')
    x3 = high_and_low("1 9 3 4 -5")
    print(x3)
    if x3 == (9, -5):
        print('test3-OK: ', x3)
    else:
        print('test3-FAILD: ', x3)
    print('*************************')


test_min_max()
# '''

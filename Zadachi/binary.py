
def add_binary(a, b):
    # x = int(input("Введите натуральное число 1: "))
    # z = int(input("Введите натуральное число 2: "))
    sum = a + b
    n = ""
    while sum > 0:
        y = str(sum % 2)
        n = y + n
        sum = int(sum / 2)
    return n


# add_binary(5, 45)

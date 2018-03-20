'''
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
(maskify("Nananananananananananananananana Batman!") ==
"####################################man!")

'''


def maskify(cc):
    a = len(cc)
    # print(cc)
    # print(cc[a - 4:a])
    if a >= 4:
        temp = ''
        # print(a)
        for i in cc[0: -4]:
            temp += '#'
        return str((temp + cc[a - 4: a]))
    else:
        return (str(cc))


maskify('4556364607935616')

if __name__ == "main":
    pass

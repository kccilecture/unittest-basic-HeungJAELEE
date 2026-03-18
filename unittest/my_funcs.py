def odd_even(a):
    if a % 2 == 1:
        b = False
    else:
        b = True
    return b


def cal_mean(a):
    b = 0
    for i in a:
        b += i
    c = b / len(a)
    return float(c)


def cal_max(a):
    b = a[0]
    for i in a:
        if i > b:
            b = i
        else:
            b = b
    return float(b)


def cal_min(a):
    b = a[0]
    for i in a:
        if i < b:
            b = i
        else:
            b = b
    return float(b)

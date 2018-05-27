def fact(x):
    sum = 1
    while (x > 0):
        sum *= x
        x = x - 1
    return sum


def comb(n, r):
    h = fact(n) / (fact(r) * fact(n - r))
    print(int(h))


comb(5, 2)

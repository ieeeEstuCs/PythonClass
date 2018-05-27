def fact(x):
    sum = 1
    while (x > 0):
        sum *= x
        x = x - 1
    print(sum)


fact(5)

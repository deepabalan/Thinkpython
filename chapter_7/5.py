# estimating value of pi.


def fact(k):
    if k == 0:
        return 1
    else:
        return k * fact(k - 1)


def val_pi(k):
    res = 0
    while k <= 1e-15:
        res = (fact(4 * k) * (1103 + 26390 * k)) / pow((fact(k), 4)) * pow(396, 4 * k)
    print res

print val_pi(1e-23)

# given 0.5, return 1 / 2 ...

from math import gcd

def get_fraction(n):
    denom = int(10e6)
    nume = int(n * denom)
    divisor = gcd(denom, nume)

    return nume // divisor, denom // divisor

print('{}/{}'.format(*get_fraction(0.5)))

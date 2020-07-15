def _fact(a, b):
    if b == 0:
        return a
    return _fact(a * b, b - 1)



def fact(n):
    return _fact(1, n)


for i in range(20):
    print(fact(i))

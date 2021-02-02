from functools import partial

def avg_three(a, b, c):
    return (a + b + c) / 3

def cap(n, s=[avg_three]):
    if len(s) == 3:
        return s[-1]()
    s.append(partial(s[-1], n))
    return cap

def curried_avg(n):
    return lambda x: lambda y: (n + x + y) / 3

# print(cap(5)(4)(3))
# print(partial(partial(partial(avg_three, 5), 4), 3)())
# print(partial(partial(avg_three, 5), 4)(3))
print(cap(5)(4)(3))


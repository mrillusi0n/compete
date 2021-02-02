from functools import partial

def avg_three(a, b, c):
    return (a + b + c) / 3

cap = partial(partial, partial, avg_three)

def curried_avg(n):
    return lambda x: lambda y: avg_three(x, y, n)

# print(cap(5)(4)(3))
# print(partial(partial(partial(avg_three, 5), 4), 3)())
# print(partial(partial(avg_three, 5), 4)(3))
# print(partial(p_func, 4)(3))
# print(q_func(3))

print(cap(5)(4)(3))
# print(cap(5))

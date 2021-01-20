def map_append(x, xs):
    return map(lambda l: [x] + l, xs)

def powerset(lst):
    if lst == []:
        return [[]]

    prev_pow = powerset(lst[1:])

    return prev_pow + list(map_append(lst[0], prev_pow))

print(list(powerset([1, 2, 3])))

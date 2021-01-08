# implement join with reduce

from functools import reduce, partial

def join(delim, itr):
    return reduce(lambda acc, item: acc + delim + item, itr)

def join(delim, itr):
    return reduce(partial(str.format, '{1}{0}{2}', delim), itr)

print(join('*', 'string'))

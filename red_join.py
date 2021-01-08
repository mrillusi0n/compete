# implement join with reduce

from functools import reduce, partial

def join(delim, itr):
    return reduce(lambda acc, item: f'{acc}{delim}{item}', itr)

def join(delim, itr):
    return reduce(partial(str.format, '{1}{0}{2}', delim), itr)

def join(delim, itr):
    # from 07734willy
    return reduce(f'{{}}{delim}{{}}'.format, itr)

print(join('*', 'string'))

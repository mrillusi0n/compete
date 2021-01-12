# return a generator of square numbers

from itertools import count
from functools import partial

def get_squares():
    return map(partial(pow, exp=2), count(1))

from itertools import tee
from operator import mul

def get_squares():
    return map(mul, *tee(count(1)))

squares = get_squares()

for i in range(10):
    print(next(squares))


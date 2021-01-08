# return a generator of square numbers

from itertools import count

def get_squares():
    return map(int(2).__pow__, count())

squares = get_squares()

for i in range(10):
    print(next(squares))


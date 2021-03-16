from itertools import accumulate
from operator import add
import random

def twine(one, two):
    new = [' ' for _ in range(len(one) + len(two))]

    for i, x in enumerate(one):
        new[i*2] = x

    for i, x in enumerate(two):
        new[i*2+1] = -x

    return new

def solve(nums):
    min_, max_ = special_min_max(nums)
    gh = abs(min_) + max_ + 3
    gw = sum(nums) * 2 + 1
    sr = max_ + 3
    sc = 0
    dr = -1
    ar = [[' ']*gw for _ in range(gh)]

    for num in nums:
        for _ in range(num):
            sr += dr
            ar[sr][sc] = '/' if dr == -1 else '\\'
            sc += 1
        sr += dr
        dr = -dr

    max_point = ar[3].index('/')

    for line in ar:
        line.insert(max_point+1, ' ')

    ar[2][max_point] = '<'
    ar[2][max_point+2] = '>'

    ar[1][max_point] = '/'
    ar[1][max_point+1] = '|'
    ar[1][max_point+2] = '\\'

    ar[0][max_point+1] = 'o'

    return paint_grid(ar)


def special_min_max(nums):
    twins = list(accumulate(twine(nums[::2], nums[1::2]), add))
    return min(twins), max(twins)


def paint_grid(grid):
    return '\n'.join(''.join(x) for x in grid)

test = [4, 1, 2, 7, 10, 6, 2, 4, 5, 6, 8, 9]

# print(test)
# print(list(accumulate(test)))
# print(solve(test))
# print(special_min_max(test))
print(solve([random.randint(0, 9) for _ in range(10)]))


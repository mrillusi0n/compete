from pprint import pprint

def explore(area, r, c):
    if area[r][c] == 'x':
        return 0

    offsets = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    area[r][c] = 'x'


    for roff, coff in offsets:
        if area[(nr := r + roff)][(nc := c + coff)] == '1':
            explore(area, nr, nc)

    return 1

lines = '''\
5 5
1 1 0 0 0
1 1 1 0 0
0 1 1 0 0
0 1 1 0 1
1 0 0 1 1'''

dims, *lines = lines.replace('0', 'x').split('\n')

rows, cols = [int(x) + 2 for x in dims.split()]

grid = [['x'] + line.split() + ['x'] for line in lines]
pad = [['x'] * cols]
grid =  pad + grid + pad


# count = 0
# for i, row in enumerate(grid):
#     for j, cell in enumerate(row):
#         if cell == '1':
#             count += explore(grid, i, j)

print(sum(explore(grid, i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '1'))


# print(count)

from pprint import pprint

def explore(area, r, c):
    if area[r][c] == 'x':
        return 0

    area[r][c] = 'x'

    for i in range(4):
        vec = 1j ** i
        if area[(nr := r + int(vec.imag))][(nc := c + int(vec.real))] == '1':
            explore(area, nr, nc)

    return 1

def get_num_blocks(area):
    return sum(explore(area, i, j) for i, row in enumerate(area) for j, cell in enumerate(row) if cell == '1')

def solve(data):
    dims, *lines = data.replace('0', 'x').split('\n')
    rows, cols = [int(x) + 2 for x in dims.split()]

    grid = [['x'] + line.split() + ['x'] for line in lines]
    pad = [['x'] * cols]
    grid =  pad + grid + pad

    return get_num_blocks(grid)

def main():
    lines = '''\
    5 5
    1 1 0 0 1
    1 1 1 0 1
    0 1 1 0 0
    0 1 1 0 1
    1 0 0 1 1'''

    print(solve(lines))


if __name__ == '__main__':
    main()

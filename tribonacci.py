# 1 1 1 3 5 9 17 ...

def trib(n):
    return _trib(n, {0: 0, 1: 1, 2: 1, 3: 1})

def _trib(n, mem):
    try:
        return mem[n]
    except KeyError:
        mem[n] = sum(_trib(n - i, mem) for i in range(1, 4))

    return mem[n]

for i in range(6):
    print(trib(i))

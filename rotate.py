# rotation

# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

def rotate(m):
    return [list(reversed(x)) for x in zip(*m)]

IMAGE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(rotate(IMAGE))

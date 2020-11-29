# buggy bar codes

from collections import Counter

def restore_bar(code, rows, _):
    maxes = [Counter(x).most_common()[0][0] for x in zip(*code)]
    return '\n'.join([''.join(x) for x in zip(*[m * rows for m in maxes])])

t = '''\
5 10
||  |||| |
||   |||||
||| |||| |
||  | || |
 || |||| |\
'''.split('\n')

print(restore_bar(t[1:], *map(int, t[0].split())))


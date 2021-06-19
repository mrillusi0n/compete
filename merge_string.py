######################### AABCAAADA

from collections import OrderedDict 

def remove_duplicates(block):
    """
    >>> remove_duplicates('AAB')
    >>> 'AB'
    """

    freq = OrderedDict()

    for c in block:
        freq[c] = freq.get(c, 0) + 1

    return ''.join(freq.keys())

def solve(text, block_size):
    return '\n'.join(map(remove_duplicates,
[text[i:i+block_size] for i in range(0, len(text), block_size)]))



print(solve('AABCAAADA', 3))

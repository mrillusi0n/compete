"""
John works at a clothing store.
He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors.
There is one pair of color  and one of color.
There are three odd socks left, one of each color.
The number of pairs is.
"""

def count_match_pairs(socks):
    count = 0
    matches = set()

    for sock in socks:
        if sock in matches:
            count += 1
            matches.remove(sock)
        else:
            matches.add(sock)

    return count

# The Ugly One

def sockMerchant(n, ar):
    f = {}

    for i in ar:
        f[i] = f.get(i, 0) + 1
    
    count = 0
    for k, v in f.items():
        count += v // 2

    return count

print(count_match_pairs([10, 20, 20, 10, 10, 30, 50, 10, 20]))


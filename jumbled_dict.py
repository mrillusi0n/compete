def special_sort(alphabet, s):
    a = {c: i for i, c in enumerate(alphabet)}
    return ''.join(sorted(list(s), key=lambda x: a[x.lower()]))

a = 'wvutsrqponmlkjihgfedcbaxyz'
t = 'camelCasE'

print(special_sort(a, t))


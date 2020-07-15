# reverse the stuff inside parens

# (foo) -> (oof)
# foo(bar) -> foorab
# foo(bar(baz)) -> foo(barzab) -> foobazrab

from matching_paren import find_match

def _preverse(s, o, c):
    i = s.find('(')
    j = find_match(s, i)

    if i == -1:
        return s[::-1]

    return (s[:o] + _preverse(s[i+1:j], i, j) + s[j+1:])[::-1]

def preverse(s):
    res = ''
    i = 0
    j = 0

    while i < len(s):
        temp = s[i]

        if temp == '(':
            j = find_match(s, i)
            temp = _preverse(s[i+1:j], i, j)
            i = j

        res += temp
        i += 1

    return res


tests = [
    '(foo)',
    'foo(bar)fizz',
    'foo(bar(baz)fizz)',
    'foo'
]

for t in tests:
    print(preverse(t))

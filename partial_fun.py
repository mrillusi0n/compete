# Given a list of strings, and a list of corresponding letters, produce an iterable indicating how many times a letter occurs in its respective string

from functools import partial

strings = ["apples", "bananas", "oranges", "grapes"]
letters = ["p", "a", "l", "p"]

def l_get_counts(strings, letters):
    return map(lambda s, l: s.count(l), strings, letters)

def s_get_counts(strings, letters):
    return map(str.count, strings, letters)

def p_get_counts(strings, letters):
    return map(partial.__call__, map(partial(partial, str.count), strings), letters)

print(list(l_get_counts(strings, letters)))
print(list(s_get_counts(strings, letters)))
print(list(p_get_counts(strings, letters)))


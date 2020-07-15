def find_match(s, o):
    p = 1

    for i, c in enumerate(s[o+1:], o+1):
        if c == '(':
            p += 1
        elif c == ')':
            p -= 1

        if p == 0:
            return i

    return 0


if __name__ == '__main__':
    tests = ['()', '(())', '(())()']

    for t in tests:
        print(find_match(t, 0))

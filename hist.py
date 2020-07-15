def vert_hist_plot(data):
    f = [0 for _ in range(26)]

    for o in data:
        if o.isalpha():
            f[ord(o) - 65] += 1

    max_val = max(f)
    curr_max = max_val
    i_chars = [i for i, x in enumerate(f) if x > 0]

    for _ in range(max_val):
        for i in i_chars:
            if f[i] >= curr_max:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

        curr_max -= 1

    for i in i_chars:
        print(chr(i + 65), end=' ')

    print()

def _vert_hist_plot(data):
    f = {}

    for o in data:
        if o.isalpha():
            f[o] = f.get(o, 0) + 1

    max_val = max([v for v in f.values()])
    curr_max = max_val

    for _ in range(max_val):
        for k, v in f.items():
            if v >= curr_max:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

        curr_max -= 1

    print(*f)


ip = "XXY YY ZZZ123ZZZ AAA BB C"
vert_hist_plot(ip)


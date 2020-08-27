def digit_set(n):
    ds = set()

    while n:
        ds.add(n % 10)
        n //= 10

    return ds


def get_next(n):
    global NUMS

    discarded = digit_set(n)
    res = 0

    while res in NUMS or digit_set(res).intersection(discarded):
        # print(f'Checking {res}...')
        # print(digit_set(res).intersection(discarded))
        res += 1

    NUMS.add(res)

    return res


nums = [i for i in range(11)]
NUMS = set(nums)

for _ in range(490):
    nums.append(get_next(nums[-1]))

print(nums[11]) # read the given index and supply here

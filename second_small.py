# find the second smallest number

def second_smallest(nums):
    return sorted(list(set(nums)))[1]

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
nums = [3, 4, 2, 1, 3, 5, 7, 0, 1, 0]

# print(second_smallest(nums))

print('\n'.join((sorted([name for name, mark in students if mark == sorted(list(set([mark for _, mark in students])))[1]]))))

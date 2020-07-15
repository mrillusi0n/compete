# Given a non-negative integer num, return the number of steps to reduce it to zero.
# If the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.

def count_steps(num):
    steps = 0

    while num != 0:
        if num % 2 == 1:
            num -= 1
        else:
            num /= 2

        steps += 1

    return steps



# A number is lucky if both
# halves of the number sum up to
# the same amount.

def is_lucky(n):
    num_digits = 0
    digit_sum = 0
    another_sum = 0
    original_num = n

    while n:
        digit_sum += n % 10
        num_digits += 1
        n //= 10

    num_digits //= 2
    n = original_num

    while num_digits:
        another_sum += n % 10
        n //= 10
        num_digits -= 1

    return another_sum == (digit_sum / 2)

print(is_lucky(1230))


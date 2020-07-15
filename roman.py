# convert dec to roman

ROMAN_CHARS = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}

ROMAN_LIST = [1, 5, 10, 50, 100, 500, 1000]

def romanize(num):
    roman_num = []
    place = 1

    while num:
        digit = (num % 10) * place
        
        if digit == upper_bound(digit)


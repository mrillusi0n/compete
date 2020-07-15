# this program eliminates vowels
# from a given string

def is_vowel(l):
    return l.lower() in { 'a', 'e', 'i', 'o', 'u' }

def remove_vowels(msg):
    res = ''

    for letter in msg:
        if not is_vowel(letter):
            res += letter 

    return res

print(remove_vowels('Oat'))


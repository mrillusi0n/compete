# unique morse

def morsify(word):
    morse_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."] 

    return ''.join([morse_letters[ord(x) - 97] for x in word])

def morse_reps(words):
    distinct = set() 

    for word in words:
        distinct.add(morsify(word))

    return len(distinct)


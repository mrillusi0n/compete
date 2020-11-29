from collections import Counter

def constructable(n, l):
  return not (Counter(l) - Counter(n))



newspaper = "Hello Pramp!"
letter = "llHrampo!"

print(constructable(newspaper, letter))

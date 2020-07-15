# Reverse the order of words

def rev_words(sentence):
	words = sentence.split()
	return ' '.join(words[::-1])

sentence = 'perfect makes practice';

res = rev_words(sentence)
print(len(res))

for c in sentence:
	print(f"'{c}', ", end='')
# Find the maximum number of nuts
# that can be collected.

# S N N S N -> 2 (K = 1)
# N N S S N S -> 3 (K = 2)

def get_max_nuts(state, k):
	counts = {'S': 0, 'N': 0}

	for o in state:
		counts[o] += 1

	return abs(counts['S'] - counts['N'] - k)

print(get_max_nuts())

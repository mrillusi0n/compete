'''
For each test case, output a single line containing a space-delimited list
of starting indices (-indexed) of substrings of  which are
matching with  according to the condition mentioned above.
The indices have to be in increasing order.
If there is no matching substring, output No Match!.
'''

def check(p, v):
	i = 0
	j = -1
	k = len(v) - 2
	flag = 'No Match!'

	while i <= len(p) - len(v):
		error = 0
		j += 1
		k += 1
		while error < 2 and j < k:
			if p[j] != v[j]:
				error += 1
			if p[k] != v[k]:
				error += 1
			k -= 1
			j += 1
		if error < 2:
			print(i, end=' ')
			flag = ''
		i += 1

	print()

if __name__ == '__main__':
	check('abbab', 'ba')

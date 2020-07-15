'''
Easy Fibonacci
'''

FIB_SEQ = {0: 0, 1: 1}
D = []

def get_fib(n):
	try:
		res = FIB_SEQ[n]
	except KeyError:
		res = get_fib(n - 2) + get_fib(n - 1)
		FIB_SEQ[n] = res

	return res

def trunc(l, size):
	if size == 1:
		return l[0]
	return trunc([l[i] for i in range(1, size, 2)], size // 2)


if __name__ == '__main__':
	for _ in range(int(input())):
		for i in range(int(input())):
			D.append(get_fib(i) % 10)

		print(trunc(D, i + 1))

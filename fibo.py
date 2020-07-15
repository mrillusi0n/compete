# Fibonacci Words

n = int(input())
a, b, c = input().split()

c = int(c)

fib = {1: (a, len(a)), 2: (b, len(b))}

def get_fib_index(n):
	curr = 1
	res = ''

	while n > fib[curr][1]:
		curr += 1
		res = get_fib(curr)

	return res


def get_fib(n):
	try:
		res = fib[n]
	except KeyError:
		p1 = get_fib(n - 2)
		p2 = get_fib(n - 1)
		res = p1[0] + p2[0]
		fib[n] = (res, p1[1] + p2[1])

	return res

print(get_fib_index(c)[c-1])

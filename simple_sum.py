# Given n, m: Find sum_cubes(n) modulo m

def sum_cubes(n):
	return int((n ** 2 * (n + 1) ** 2) / 4)

for _ in range(int(input())):
	n, m = map(int, input().split())
	print(sum_cubes(n) % m)
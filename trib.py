f=lambda n:bool(n)if n<3 else f(n-1)+f(n-2)+f(n-3)

for i in range(8):
    print(f(i))

# 0 1 2 -> 0 1 1

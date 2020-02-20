def f(x):
    return x + 1

n = int(input())
b = {}
for i in range(n):
    a = int(input())
    if a in b:
        print(b[a])
    else:
        b[a] = f(a)
        print(b[a])

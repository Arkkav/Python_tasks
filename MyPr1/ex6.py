j = 0
a = []
b = []
c = []
fl = True
while fl:
    a = [i for i in input().split()]
    # b [j] += a
    if a == ['end']:
        fl = False
    else:
        b.append(a)
        j += 1
c = [[0 for j in range(len(b[i]))]for i in range(len(b))]
n = len(b)
for i in range(n):
    m = len(b[i])
    for j in range(m):
        c[i][j] = int(b[i - 1][j]) + int(b[i - n + 1][j]) + int(b[i - n][j - 1]) + int(b[i][j - m + 1])
    print(*c[i])

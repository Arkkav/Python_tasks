lst = [int(i) for i in input().split()]
x = int(input())
a = []
j = 0
for i in lst:
    if i == x:
        a += [j]
    j += 1
if a == []:
    print('Отсутствует')
else:
    print(*a)


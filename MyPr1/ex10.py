
lst = [i.lower() for i in input().split()]
s = {}
for i in lst:
    if s.get(i) == None:
        s[i] = 1
    else:
        s[i] += 1
print(*[i + ' ' + str(s[i]) for i in s], sep='\n')
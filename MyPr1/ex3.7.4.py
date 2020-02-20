a = ('\n'.join(input().lower() for i in range(int(input())))).split('\n')
x = 0
y = 0
for s in a:
	if s[0:2] == 'юг':
		y -= int(s[3:])
	elif s[0:5] == 'запад':
		x -= int(s[6:])
	elif s[0:6] == 'восток':
		x += int(s[7:])
	elif s[0:5] == 'север':
		y += int(s[6:])
print(str(x) + ' ' + str(y))

# s = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
# for i in range(int(input())):
#     k = input().split()
#     s[k[0]] += int(k[1])
# print(s['восток'] - s['запад'], s['север'] - s['юг'])
s = input()
a = input()
b = input()
s1 = ''
if a == b and a in s:
	print('Impossible')
else:
	for i in range(1001):
		s1 = s.replace(a, b)
		if s == s1:
			print(i)
			break
		elif i == 1000:
			print('Impossible')
			break
		else:
			s = s1


ans = 0
n = len(objects)
for i in range(n): # доступная переменная objects
	f = True
	for j in range(i + 1, n):
		if objects[i] is objects[j]:
			f = False
			break
	if f:
		ans += 1
print(ans)

# print(len(set(map(id, objects))))
# print(len(set(id(i) for i in objects)))
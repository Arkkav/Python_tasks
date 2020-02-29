n, k = map(int, input().split())
def c_rec(n, k):
	if k == 0:
		return 1
	elif k > n:
		return 0
	else:
		return c_rec(n - 1, k) + c_rec(n - 1, k - 1)
y = c_rec(n, k)
print(y)
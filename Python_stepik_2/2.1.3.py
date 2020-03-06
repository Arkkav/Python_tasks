class NonPositiveError(Exception):
	pass


class PositiveList(list):
	def append(self, x):
		if x <= 0:
			raise NonPositiveError('NonPositiveError')
		super().append(x)


g = PositiveList()
g.append(-1)
print(g)
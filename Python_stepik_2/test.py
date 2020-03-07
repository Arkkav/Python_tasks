import operator as op

# x = {1: 'a', 2: 'abc', 3: 'ab'}
# print(x.items())
x = [1, 2, 3]
f = op.itemgetter(1)
print(f(x))

f = op.attrgetter('sort')
print(f([]))
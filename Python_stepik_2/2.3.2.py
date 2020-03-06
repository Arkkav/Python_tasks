import math
import itertools

def primes():
	count = 2

	while True:
		isprime = True

		for x in range(2, int(math.sqrt(count) + 1)):
			if count % x == 0:
				isprime = False
				break

		if isprime:
			yield count

		count += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))

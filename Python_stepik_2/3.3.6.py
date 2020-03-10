import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	print(re.sub("human", "computer", line))


# print(re.sub(r'human', 'computer', sys.stdin.read()), end='')
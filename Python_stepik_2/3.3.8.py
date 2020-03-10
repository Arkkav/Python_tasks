import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	print(re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line))

# #!!
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'\b(\w)(\w)', r"\2\1", line))
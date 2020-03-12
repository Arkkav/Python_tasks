import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	s = re.fullmatch(r"(1(01*0)*1|0)*", line)
	if s is not None:
		print(s[0])
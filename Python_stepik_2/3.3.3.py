import re
import sys

pattern = r"z.{3}z"
for line in sys.stdin:
	line = line.rstrip()
	match_object = re.search(pattern, line)
	if match_object is not None:
		print(line)
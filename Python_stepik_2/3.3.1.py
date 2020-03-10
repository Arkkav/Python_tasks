import re
import sys

pattern = r"cat"
for line in sys.stdin:
	line = line.rstrip()
	match_object = re.findall(pattern, line)
	if len(match_object) >= 2:
		print(line)

#catcatsghdtscat
# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"cat.*cat", line):
#         print(line)
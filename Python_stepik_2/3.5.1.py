import csv

with open("Crimes.csv", 'r') as f:
	reader = csv.reader(f)
	r = (i[5] for i in reader if '2015' in i[2])
	d = dict()
	for word in r:
		if word in d:
			d[word] += 1
		else:
			d[word] = 0
	d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],  reverse=True)}
	print(d)

# import csv
# from collections import Counter as c
#
# with open('Crimes.csv') as f:
# 	data = csv.reader(f)
# 	print(c( row[5] for row in data if '2015' in row[2] ))


# import csv
# from collections import Counter as c
#
# with open('Crimes.csv') as f:
#   result = c(row[5] for row in csv.reader(f))
#   print(result.most_common(1))
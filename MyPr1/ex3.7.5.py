with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3380_5.txt', 'r') as file1:
	d = {'1' : [0, 0], '2' : [0, 0], '3' : [0, 0], '4' : [0, 0], '5' : [0, 0], '6' : [0, 0], '7' : [0, 0], '8' : [0, 0], '9' : [0, 0], '10' : [0, 0], '11' : [0, 0]}
	a = file1.read().strip().split('\n')
	a = [i.split() for i in a]
for ai in a:
	d[ai[0]][0] += int(ai[2])
	d[ai[0]][1] += 1
for key in d:
	if d[key] == [0, 0]:
		d[key] = '-'
	else:
		d[key] = str(d[key][0] / d[key][1])
print(*[i + ' ' + d[i] for i in d], sep='\n')

# d = {i: [] for i in range(1,12)}
# with open(r'D:\Новая папка\dataset_3380_5.txt','r', encoding='utf-8') as f1:
#   for i in f1:
#     d[int(i.split()[0])].append(float(i.split()[2]))
#
# for i in range(1,12):
#   if d[i]:
#     print(i, sum(d[i])/len(d[i]))
#   else:
#     print(i, '-')
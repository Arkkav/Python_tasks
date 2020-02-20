# import os
# s = ''
# t = ''
# num = '1'
# with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_2.txt', 'r') as inf:
#     line = inf.readline().strip()
#     for i in range(len(line)):
#         if line[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
#             num += line[i]
#         elif t != '':
#             s += t * int(num)
#             t = line[i]
#             num = ''
#         else:
#             t = line[i]
#             num = ''
#     s += t * int(num)
# with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_2.txt', 'w') as inf:
#     inf.write(s + '\n')


s, d = 'D8s11T20s13r16V8O9o11f3V3S5B14T11m12n18i17T18x15d17V1b5l2x13I5t12q7c14', []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')
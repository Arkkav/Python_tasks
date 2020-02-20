# s = ''
# a = []
# line = ''
# with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_3.txt', 'r') as inf:
#     for line in inf:
#         line += line.strip().lower() + ' '
#     for ltr in line:
#         if ltr != ' ':
#             s += ltr
#         else:
#              a.append(s)
#              s = ''
# s = {}
# max = 0
# max_w = ''
# for i in a:
#     if s.get(i) == None:
#         s[i] = 1
#     else:
#         s[i] += 1
#         if max < s[i]:
#             max = s[i]
#             max_w = i
#
# print(max_w, s[max_w], sep=' ')

with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_3.txt', 'w') as inf:
    inf.write('12\n')
    inf.write('1234\n')
with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_3.txt', 'r') as inf:
    line = inf.read()
print(line)
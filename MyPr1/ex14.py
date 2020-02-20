# with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_4.txt', 'r') as inf:
#     a = []
#     a = inf.read().strip().split('\n')
#     for i in range(len(a)):
#         a[i] = a[i].split(';')
# b = len(a)
# with open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_4.txt', 'w') as inf:
#     [inf.write(str((int(mat) + int(phys) + int(rus)) / 3) + '\n') for lname, mat, phys, rus in a]
#     inf.write(str(sum([int(math) for lname, math, phys, rus in a]) / b) + ' ' + str(sum([int(phys) for lname, math, phys, rus in a]) / b) + ' ' + str(sum([int(rus) for lname, math, phys, rus in a]) / b))

   # [print((int(mat) + int(phys) + int(rus)) / 3) for lname, mat, phys, rus in a]
   #  print(str(sum([int(math) for lname, math, phys, rus in a]) / b) + ' ' + str(sum([int(phys) for lname, math, phys, rus in a]) / b) + ' ' + str(sum([int(rus) for lname, math, phys, rus in a]) / b))
st = [x.split(';') for x in open(r'C:\Users\arkka\PycharmProjects\MyPr1\dataset_3363_4.txt').readlines()]
print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])
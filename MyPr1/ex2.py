numbers = [int(i) for i in input().split()]
numbers.sort()
j = 0
flag_1 = False
while len(numbers) - 1 > j:
    if numbers[j] == numbers[j + 1]:
        flag_1 = True
        del numbers[j + 1]
    elif not flag_1:
        del numbers[j]
    else:
        flag_1 = False
        j += 1
if j == len(numbers) - 1 and flag_1 == False:
    del numbers[j]
for i in numbers:
    print(str(i), end=' ')

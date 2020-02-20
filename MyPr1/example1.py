numbers = [int(i) for i in input().split()]
sums = ''
l = len(numbers)
if l == 1:
    sums = str(numbers[0])
else:
    j = 0
    while j < l - 1:
        sums += str(numbers[j - 1] + numbers[j + 1]) + ' '
        j += 1
    sums += str(numbers[l - 2] + numbers[0])
print(sums)
sum1 = 0
sum2 = 0
while True:
    a = int(input())
    sum1 += a
    sum2 += a ** 2
    if sum1 == 0:
        break
print(sum2)
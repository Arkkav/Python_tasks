n = int(input())
tab = [input().split(';') for i in range(n)]
d = {}
for i in tab:
    if i[0] not in d:
        d[i[0]] = [0]*4
    if i[2] not in d:
        d[i[2]] = [0] * 4
    if i[1] > i[3]:
        d[i[0]][1] += 1
        d[i[2]][3] += 1
        d[i[0]][0] += 1
        d[i[2]][0] += 1
    elif i[1] < i[3]:
        d[i[0]][3] += 1
        d[i[2]][1] += 1
        d[i[0]][0] += 1
        d[i[2]][0] += 1
    else:
        d[i[0]][2] += 1
        d[i[2]][2] += 1
        d[i[0]][0] += 1
        d[i[2]][0] += 1

#Всего_игр - Побед - Ничьих - Поражений - Всего_очков

print(*[i + ':' + str(d[i][0]) + ' ' + str(d[i][1]) + ' ' + str(d[i][2]) + ' ' + str(d[i][3]) + ' ' + str((d[i][1]*3 + d[i][2])) for i in d], sep='\n')

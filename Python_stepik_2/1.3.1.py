def closest_mod_5(x):
	return (x if x % 5 == 0 else x + (5 - x % 5))
print(closest_mod_5(int(input())))

# closest_mod_5 = lambda x: (x + 4) // 5 * 5

# a=1
# b=2
# lst = [5,6,7,8]
# dct = {"1":11,"2":22}
# print(a, b, lst, dct)
#
# def pr(aa, bb, cc, *llst, **ddct):
#     print(aa) #=a
#     print(bb) #=b
#     print(cc) #возьмётся из списка
#     print(llst) #остатки списка в виде кортежа
#     print(lst) #глобальная переменная
#     for k in ddct:
#         print(k, ddct[k])
#     print(ddct) #словарь в к-й попали dct, r=8,t=6
#     print(*llst) #элементы кортежа
#     print(*ddct) #ключи словаря
#     print(*dct) #глобальная переменная
# pr(a, b, *lst, **dct, r=8,t=6)
# 1 2 [5, 6, 7, 8] {'1': 11, '2': 22}
# 1
# 2
# 5
# (6, 7, 8)
# [5, 6, 7, 8]
# 1 11
# 2 22
# r 8
# t 6
# {'1': 11, '2': 22, 'r': 8, 't': 6}
# 6 7 8
# 1 2 r t
# 1 2

Код проверки времени выполнения функций
import time
def one(a, b, c):
	return a + b + c


def two(*args):
	return args[0] + args[1] + args[2]
count = 9000000
_startTime = time.time()
for num in range(count):
	one(1, 2, 3)
print("Positional test:", time.time() - _startTime)

_startTime = time.time()
for num in range(count):
	two(1, 2, 3)
print("Positional args as list test:", time.time() - _startTime)
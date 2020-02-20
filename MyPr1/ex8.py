
# def modify_list(l):
#     i = 0
#     while True:
#         if l[i] % 2 != 0:
#             del l[i]
#         else:
#             i += 1
#         if i > len(l) - 1:
#             break
#     for i in range(len(l)):
#         l[i] //= 2
# def modify_list(l):
#     l[:] = [i//2 for i in l if not i % 2]


# lst = lst[:]
# modify_list(lst)

lst = [1, 2, 3, 4, 5, 6]
# def modify_list(l):
#     for i in range(len(l)):
#         print(list(range(len(l))))
#         if l[i] % 2 == 1:
#             del l[i]
#         else:
#             l[i] //= 2

modify_list(lst)
print(lst)
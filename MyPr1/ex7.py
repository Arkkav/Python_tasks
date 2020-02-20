# n = int(input())
# n2 = n ** 2
# b = [[0 for j in range(n)] for i in range(n)]
# # b[0] = [i + 1 for i in range(n)]
# dir_i = 0
# dir_j = 1
# p_i = 0
# p_j = 0
# val = 0
# # for i in range(1 + 2 * (n - 1)):
# the_end = False
# while not the_end:
#     val += 1
#     b[p_i][p_j] = val
#     if 0 <= p_i + dir_i <= n - 1 and 0 <= p_j + dir_j <= n - 1:
#         if b[p_i + dir_i][p_j + dir_j] != 0:
#             if dir_i == 0 and dir_j == 1:
#                 dir_i = 1
#                 dir_j = 0
#             elif dir_i == 1 and dir_j == 0:
#                 dir_i = 0
#                 dir_j = -1
#             elif dir_i == 0 and dir_j == -1:
#                 dir_i = -1
#                 dir_j = 0
#             elif dir_i == -1 and dir_j == 0:
#                 dir_i = 0
#                 dir_j = 1
#     else:
#         if dir_i == 0 and dir_j == 1:
#             dir_i = 1
#             dir_j = 0
#         elif dir_i == 1 and dir_j == 0:
#             dir_i = 0
#             dir_j = -1
#         elif dir_i == 0 and dir_j == -1:
#             dir_i = -1
#             dir_j = 0
#         elif dir_i == -1 and dir_j == 0:
#             dir_i = 0
#             dir_j = 1
#     if b[p_i + dir_i - n][p_j + dir_j - n] != 0:
#         the_end = True
#     p_i += dir_i
#     p_j += dir_j
# [print(*b[i], sep=' ') for i in range(n)]
#
n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])
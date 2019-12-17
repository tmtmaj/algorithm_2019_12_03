# import sys
# cmd = lambda: sys.stdin.readline()
#
# def x_func(e_list):
#     e_list = e_list
#     x_list = [0 for _ in range(len(e_list))]
#
#     for i in range(len(e_list)):
#         for j in range(i + 1, len(e_list)):
#             if (e_list[i][0] > e_list[j][0] and e_list[i][1] < e_list[j][1]) or (e_list[i][0] < e_list[j][0] and e_list[i][1] > e_list[j][1]):
#                 x_list[i] += 1
#                 x_list[j] += 1
#
#     return x_list
#
#
# N = int(cmd().strip())
# e_list = []
# cnt = 0
#
# for _ in range(N):
#     e_list.append(list(map(int, cmd().strip().split())))
#
# x_list = [0 for _ in range(N)]
#
# # print(e_list)
# for i in range(N):
#     for j in range(i+1, N):
#         if (e_list[i][0] > e_list[j][0] and e_list[i][1] < e_list[j][1]) or (e_list[i][0] < e_list[j][0] and e_list[i][1] > e_list[j][1]):
#             x_list[i] += 1
#             x_list[j] += 1
#
# # print(x_list)
#
# while max(x_list) != 0:
#     max_x = max(x_list)
#     max_x_index = x_list.index(max_x)
#     del e_list[max_x_index]
#     x_list = x_func(e_list)
#     cnt += 1
#     print(x_list)
# print(e_list)
#
# print(cnt)

import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
e_list = [list(map(int, cmd().strip().split())) for _ in range(N)]
e_list.sort(key = lambda x: x[0])

lis = [1]
for i in range(1, N):
    lis.append(1)
    for j in range(i):
        if e_list[i][1] > e_list[j][1] and lis[j] + 1 > lis[i]:
            lis[i] = lis[j] + 1

print(N - max(lis))
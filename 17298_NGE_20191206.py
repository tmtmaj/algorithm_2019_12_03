# import sys
# import copy
# cmd = lambda: sys.stdin.readline()
#
# N = int(cmd().strip())
# in_list = [int(num) for num in cmd().strip().split(" ")]
#
# # print(N, in_list)
#
# NGE_list = []
#
# for num in range(N):
#     temp_N = N
#     temp_list = copy.deepcopy(in_list)
#     ori_num = temp_list[num]
#     real_NGE = ori_num
#     for _ in range(num+1, N):
#
#         NGE = temp_list.pop()
#         # print(ori_num, NGE, real_NGE)
#         if NGE > ori_num:
#             real_NGE = NGE
#
#     if ori_num == real_NGE:
#         NGE_list.append(-1)
#     else:
#         NGE_list.append(real_NGE)
#
#
# print(" ".join([str(i) for i in NGE_list]))
#
#
#
# import sys
# import copy
# cmd = lambda: sys.stdin.readline()
#
# N = int(cmd().strip())
# in_list = [int(num) for num in cmd().strip().split(" ")]
#
# # print(N, in_list)
#
# NGE_list = [-1 for _ in range(N)]
#
# for num in range(N):
#     ori_num = in_list[num]
#
#     for num2 in range(num, N):
#         if ori_num < in_list[num2]:
#             NGE_list[num] = in_list[num2]
#             break
#
#
# print(" ".join([str(i) for i in NGE_list]))

import sys
import copy
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
in_list = [int(num) for num in cmd().strip().split(" ")]

# print(N, in_list)

NGE_list = [-1 for _ in range(N)]
stack = []

for num in range(N):

    NGE_list[stack.pop()]
    stack.append(num)



print(" ".join([str(i) for i in NGE_list]))
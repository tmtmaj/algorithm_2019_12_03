# import sys
#
# cmd = lambda: sys.stdin.readline()
#
# A, B, C = map(int, cmd().strip().split())
#
# print((A**(B))%C)
# # print(3*2)
#
# # pow

import sys

cmd = lambda: sys.stdin.readline()

A, B, C = map(int, cmd().strip().split())
# result = 0

# def div_conq(A,B):
#
#     if B == 0:
#         return 1
#     elif B == 1:
#         return (A)
#     elif B % 2 ==0:
#         temp = (div_conq(A, B//2))
#         return temp*temp
#     else:
#         temp = (div_conq(A, (B-1)//2))
#         return (temp*temp)*A
#
# # print(div_conq(A,B))
# print(div_conq(A,B)%C)

print(pow(A,B,C))
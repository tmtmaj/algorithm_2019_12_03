# import sys
#
# cmd = lambda: sys.stdin.readline()
#
# N, K = map(int, cmd().strip().split())
# A = []
# for _ in range(N):
#     A.append(int(cmd().strip()))
#
# cnt = 0
# K_ = 0
# A.reverse()
#
# while K_ < K:
#     for n in range(N):
#         K_ += A[n]
#         if K_ <= K:
#             cnt += 1
#             break
#         else:
#             K_ -= A[n]
#
#
# print(cnt)
#

import sys

cmd = lambda: sys.stdin.readline()

N, K = map(int, cmd().strip().split())
A = []

for _ in range(N):
    A.append(int(cmd().strip()))

A.reverse()
cnt = 0

for n in range(N):
    coin = A[n]
    if K >= coin:
        cnt += K//coin
        K -= coin * (K//coin)

print(cnt)
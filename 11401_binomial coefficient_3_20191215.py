import sys

cmd = lambda: sys.stdin.readline()

N, K = map(int, cmd().strip().split())
p = 1000000007

# def div_conq(N, K):
#     if K == N:
#         return 1
#     elif K == 0:
#         return 1
#     else:
#         return div_conq(N-1,K-1) + div_conq(N-1, K)
#
# print(div_conq(N,K)%1000000007)

A = 1
B = 1

for i in range(1,N+1):
    A *= i
    A %= p

for i in range(1, K+1):
    B *= i
    B %= p

for i in range(1, N-K+1):
    B *= i
    B %= p

print(((A%p)*(pow(B, p-2, p)))%p)
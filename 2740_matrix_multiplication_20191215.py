import sys

cmd = lambda: sys.stdin.readline()

N, M = map(int, cmd().strip().split())
A = [list(map(int, cmd().strip().split())) for _ in range(N)]
M, K = map(int, cmd().strip().split())
B = [list(map(int, cmd().strip().split())) for _ in range(M)]

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k]*B[k][j]

for c in C:
    print(" ".join(map(str, c)))
    # print(*c, sep="*")


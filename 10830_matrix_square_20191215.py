import sys

cmd = lambda: sys.stdin.readline()

N, B = map(int, cmd().strip().split())
A = [list(map(int, cmd().strip().split())) for _ in range(N)]

C = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            C[i][j] = 1


def div_conq(X, Y, B):

    if B == 1:
        return div_conq(C, X, 2)

    Out = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Out[i][j] += X[i][k] * Y[k][j]
                Out[i][j] %= 1000

    if B == 2:
        return Out
    elif B % 2 == 0:
        return div_conq(Out, Out, B//2)
    else:
        return div_conq(div_conq(Out, Out, (B-1)//2), Y,2)



Out = div_conq(A, A, B)
for out in Out:
    print(*out)
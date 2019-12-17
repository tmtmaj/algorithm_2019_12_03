# import sys
#
# cmd = lambda: sys.stdin.readline()
#
# n = int(cmd().strip())
# p = 1000000
#
# def div_conq(N):
#
#     if N == 1:
#         return 0
#     elif N == 2:
#         return 1
#     elif N == 3:
#         return 1
#     else:
#         return div_conq(N-1)+div_conq(N-2) %p
#
# print(div_conq(n+1))

import sys
cmd = lambda: sys.stdin.readline()

n = int(cmd().strip())
p = 1000000

def matmul(A, B):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += (A[i][k]*B[k][j]) % p
    return C

mul_op = [[1,1],[1,0]]
answer = [[1,0],[0,1]]

n = n - 1

while(n>0):
    if(n%2 == 1):
        answer = matmul(answer, mul_op)
    mul_op = matmul(mul_op, mul_op)
    n =n//2

print(answer[0][0]% p)
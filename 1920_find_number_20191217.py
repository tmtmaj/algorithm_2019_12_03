import sys

cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
A = list(map(int, cmd().strip().split()))
M = int(cmd().strip())
B = list(map(int, cmd().strip().split()))

A.sort()
result = []

# print(A, B, M, N)
for i in range(M):
    target = B[i]
    left = 0
    right = N
    mid = (left + right )//2
    while True:
        if left== mid and A[mid] != target:
            result.append("0")
            break
        # elif target < A[0] or target > A[-1]:
        #     result.append("0")
        #     break
        # elif (mid == left and A[right] != target) or (mid == right and A[left] != target):
        #     result.append("0")
        #     break
        if (target == A[mid]):
            result.append("1")
            break
        elif target > A[mid]:
            left = mid
            mid = (right+left)//2
        elif target < A[mid]:
            right = mid
            mid = (right+left)//2

        # print(result)

for r in result:
    print(*r, sep="/n")
import sys

cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())

P = list(map(int, cmd().strip().split()))

P.sort()

sum = 0

for n in range(N):
    sum += (N-n)*P[n]

print(sum)
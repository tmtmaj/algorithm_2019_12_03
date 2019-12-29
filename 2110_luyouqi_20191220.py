import sys
cmd = lambda: sys.stdin.readline()

N, C = map(int, cmd().strip().split())
x = []

for _ in range(N):
    x.append(int(cmd().strip()))

x.sort()
max = x[-1]
min = 1
ans = 0
while max >= min:
    cnt = 1
    mid = (min+max)//2
    cur_home = x[0]
    for i in x:
        if mid <= (i - cur_home):
            cnt += 1
            cur_home = i

    if cnt >= C:
        ans = mid
        min = mid +1
    else:
        max = mid -1

print(ans)
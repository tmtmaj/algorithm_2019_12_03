import sys
cmd = lambda: sys.stdin.readline()

N, M = map(int, cmd().strip().split())
N_list = list(map(int, cmd().strip().split()))

# print(N, M , N_list)
# N_list.sort()

min = 0
max = max(N_list)
mid = 0
ans = 0

while min <= max:
    mid = (min + max)//2
    cut = 0
    for n in N_list:
        if n > mid:
            cut += n - mid
            if cut > M:
                break

    if cut < M:
        max = mid - 1

    if cut >= M:
        ans = mid
        min = mid + 1

    # else:
    #     break

print(ans)
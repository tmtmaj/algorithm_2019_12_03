import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
wine_list = [0]
out_list = [0]

for _ in range(N):
    wine_list.append(int(cmd().strip()))

if N == 1:
    out_list = [0,wine_list[1]]
else:
    out_list = [0,wine_list[1], wine_list[2]+wine_list[1]]

for n in range(3, N+1):
    case1 = out_list[n-1]
    case2 = wine_list[n-1] + wine_list[n] + out_list[n-3]
    case3 = out_list[n-2] + wine_list[n]

    out_list.append(max(case1, case2, case3))

print(out_list[N])

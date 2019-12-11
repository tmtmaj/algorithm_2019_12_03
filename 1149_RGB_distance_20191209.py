import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
in_list = []
for _ in range(N):
    in_list.append(list(map(int, cmd().strip().split())))

out_list = [[0]*3 for _ in range(N)]

out_list[0] = in_list[0]
triple = [0,1,2]
for i in range(1,N):
    for j in range(3):
        if j == 0:
            out_list[i][j] = in_list[i][j] + min(out_list[i-1][1], out_list[i-1][2])
        elif j == 1:
            out_list[i][j] = in_list[i][j] + min(out_list[i-1][0], out_list[i-1][2])
        else:
            out_list[i][j] = in_list[i][j] + min(out_list[i-1][1], out_list[i-1][0])

print(min(out_list[-1]))
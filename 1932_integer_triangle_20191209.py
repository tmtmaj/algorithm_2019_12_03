import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
triangle_list = []
al = [[0]*n for n in range(1,N+1)]

for _ in range(N):
    triangle_list.append(list(map(int, cmd().strip().split())))
al[0][0] = triangle_list[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            al[i][j] = triangle_list[i][j] + al[i-1][j]
        elif j > 0 and j < i:
            al[i][j] = max((triangle_list[i][j] + al[i-1][j]), (triangle_list[i][j] + al[i-1][j-1]))
        else:
            al[i][j] = triangle_list[i][j] + al[i-1][j-1]

print(max(al[-1]))
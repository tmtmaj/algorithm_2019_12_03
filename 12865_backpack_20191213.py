import sys
cmd = lambda: sys.stdin.readline()

N, K = map(int, cmd().strip().split())
item_list = [[0,0]]+[list(map(int, cmd().strip().split())) for _ in range(N)]

DP = [[0]*(K+1) for _ in range(N+1)]
# 이차원 배열을 만든다.
# N by K 짜리 2차원 배열
# 이중 for문을 사용, 물건의 갯수/무게의 제한량

for i in range(1,N+1):
    for j in range(1, K+1):
        # j는 무게의 제한량.
        if item_list[i][0] <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j - item_list[i][0]]+ item_list[i][1])
        else:
            DP[i][j] = DP[i-1][j]

print(DP[-1][-1])
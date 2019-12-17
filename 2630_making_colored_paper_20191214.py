import sys

cmd = lambda: sys.stdin.readline()



def div_conq(i, j, N):
    if N == 1:
        return [0, 1] if paper[i][j] == 1 else [1, 0]
    left_up = div_conq(i,j, N//2)
    right_up = div_conq(i, j + N//2, N//2)
    left_down = div_conq(i+N//2, j, N//2)
    right_down = div_conq(i+N//2, j+N//2, N//2)

    if (left_up == left_down ==right_down==right_up == [1,0]) or left_up == left_down ==right_down==right_up == [0,1]:
        return left_up
    else:
        return list(map(sum, zip(left_up,left_down,right_up,right_down)))

N = int(cmd().strip())
paper = [list(map(int, cmd().strip().split())) for _ in range(N)]

print(*div_conq(0,0,N), sep = "\n")
import sys

cmd = lambda: sys.stdin.readline()



def div_conq(i, j, N):
    if N == 1:
        if paper[i][j] == -1:
            return [1,0,0]
        elif paper[i][j] == 0:
            return [0,1,0]
        else:
            return [0,0,1]

    lu = div_conq(i, j, N//3)
    cu = div_conq(i, j + N//3, N//3)
    ru = div_conq(i, j + 2*(N//3), N//3)
    lm = div_conq(i+ N//3, j, N // 3)
    cm = div_conq(i+ N//3, j + N // 3, N // 3)
    rm = div_conq(i+ N//3, j + 2 * (N // 3), N // 3)
    ld = div_conq(i+ 2 * (N // 3), j, N // 3)
    cd = div_conq(i+ 2 * (N // 3), j + N // 3, N // 3)
    rd = div_conq(i+ 2 * (N // 3), j + 2 * (N // 3), N // 3)

    if (lu==cu==ru==lm==cm==rm==ld==cd==rd== [1,0,0]) or (lu==cu==ru==lm==cm==rm==ld==cd==rd== [0,1,0]) or(lu==cu==ru==lm==cm==rm==ld==cd==rd== [0,0,1]):
        return lu
    else:
        return list(map(sum, zip(lu,cu,ru,lm,cm,rm,ld,cd,rd)))

N = int(cmd().strip())
paper = [list(map(int, cmd().strip().split())) for _ in range(N)]

print(*div_conq(0,0,N), sep = "\n")
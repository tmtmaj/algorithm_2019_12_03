import sys

cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
Video = [list(map(int, cmd().strip())) for _ in range(N)]
result = ""

def div_conq(i, j, N):

    if N == 1:
        return "1" if Video[i][j] == 1 else "0"

    lu = div_conq(i, j, N//2)
    ru = div_conq(i, j + N//2, N//2)
    ld = div_conq(i+N//2, j, N//2)
    rd = div_conq(i+N//2, j + N//2, N//2)

    if lu == ld == ru == rd == "0" or lu == ld == ru == rd == "1":
        return str(lu)
    else:
        return "(" + str(lu) + str(ru) + str(ld) + str(rd) + ")"

print(div_conq(0,0,N))

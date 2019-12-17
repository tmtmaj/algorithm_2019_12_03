import sys
cmd = lambda: sys.stdin.readline()

fir_seq = cmd().strip()
sec_seq = cmd().strip()

LCS = [[0 for _ in range(len(sec_seq)+1)] for _ in range(len(fir_seq)+1)]

for i in range(len(fir_seq)):
    for j in range(len(sec_seq)):
        if fir_seq[i] == sec_seq[j]:
            LCS[i+1][j+1] = LCS[i][j] + 1
        else:
            LCS[i+1][j+1] = max(LCS[i+1][j], LCS[i][j+1])

print(LCS[-1][-1])
import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
answers = [[1, 0], [0, 1]]
Ts = []

for _ in range(N):
    T = int(cmd().strip())
    if T > (len(answers) - 1):
        for t in range(len(answers), T+1):
            answers.append([t2+t1 for t2, t1 in (answers[t-2], answers[t-1])])
    Ts.append(T)

for T in Ts:
    print("{} {}".format(answers[T][0], answers[T][1]))


import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
K = int(cmd().strip())

print((K    //N)*(K%N))
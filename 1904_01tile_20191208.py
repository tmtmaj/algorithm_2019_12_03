import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())

a1 = 1
a2 = 2

for n in range(2, N):
    temp_tile = a1+a2
    a1 = a2
    a2 = temp_tile % 15746

print(a2)
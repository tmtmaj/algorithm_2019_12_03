import sys

cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
point_list = []

for _ in N:
    point_list.append(list(map(int, cmd().strip().split())))


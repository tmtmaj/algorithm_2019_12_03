import sys
import copy
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
num_list = list(map(int, cmd().strip().split()))
out_right_list = [0 for _ in range(N)]
out_left_list = [0 for _ in range(N)]
out_list = []
for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j] and out_right_list[i] < out_right_list[j]:
            out_right_list[i] = out_right_list[j]
    out_right_list[i] += 1

num_list.reverse()

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j] and out_left_list[i] < out_left_list[j]:
            out_left_list[i] = out_left_list[j]
    out_left_list[i] += 1

out_left_list.reverse()

for n in range(N):
    out_list.append(out_right_list[n] + out_left_list[n] - 1)

print(max(out_list))
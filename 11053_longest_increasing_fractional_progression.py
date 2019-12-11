import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
# num_list = []

# for _ in range(N):
num_list= list(map(int,cmd().strip().split()))

out_list = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j] and out_list[i] < out_list[j]:
            out_list[i] = out_list[j]
    out_list[i] += 1

print(max(out_list))
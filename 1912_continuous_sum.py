import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
num_list = list(map(int, cmd().strip().split()))

max_sum = [num_list[0]]

for n in range(0, N-1):
    max_sum.append(max(max_sum[n] + num_list[n+1], num_list[n+1]))
# print(max_sum)
# print(num_list)
print(max(max_sum))
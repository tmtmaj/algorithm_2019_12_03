# import sys
# cmd = lambda: sys.stdin.readline()
#
# N = int(cmd().strip())
# out = 9
#
# for n in range(1, N):
#     out = (out - 2**(n-1)) *2 +2**(n-1)
#
# print(out%1000000000)

import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())

out_list = [0,1,1,1,1,1,1,1,1,1]

cnt = 1
while cnt < N:
    next = [
        out_list[1],
        out_list[0] + out_list[2],
        out_list[1] + out_list[3],
        out_list[2] + out_list[4],
        out_list[3] + out_list[5],
        out_list[4] + out_list[6],
        out_list[5] + out_list[7],
        out_list[6] + out_list[8],
        out_list[7] + out_list[9],
        out_list[8]
    ]
    out_list = next
    cnt += 1


print(sum(out_list)%1000000000)
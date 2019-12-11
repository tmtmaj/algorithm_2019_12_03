# import sys
# # cmd = lambda: sys.stdin.readline()
# #
# # X = int(cmd().strip())
# # cnt = 0
# #
# # while True:
# #     if X%3 ==0:
# #         X = X//3
# #     elif X%2 == 0:
# #         X = X//2
# #     else:
# #         X -= 1
# #     cnt += 1
# #     if X == 1:
# #         break
# #
# # print(cnt)

import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())

out_list = [0,0,1,1]

for n in range(4, N+1):
    out_list.append(out_list[n-1]+1)
    if n%2 == 0:
        out_list[n] = min(out_list[n], out_list[n//2]+1)
    if n%3 == 0:
        out_list[n] = min(out_list[n], out_list[n//3]+1)


print(out_list[N])
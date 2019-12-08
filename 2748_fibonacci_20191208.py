# import sys
# cmd = lambda: sys.stdin.readline()
#
# N = int(cmd().strip())
# a1 = 0
# a2 = 1
# for _ in range(N):
#     temp_a = a1+a2
#     a1 = a2
#     a2 = temp_a
#
#
# print(a1)

import sys
cmd = lambda: sys.stdin.readline()

fb_num = [0, 1]

N = int(cmd().strip())

for i in range(2,N+1):
    fb_num.append(fb_num[i-2] + fb_num[i-1])

print(fb_num[N])
# import sys
# cmd = lambda: sys.stdin.readline()
#
# N = int(cmd().strip())
# card_list = [i+1 for i in range(N)]
# card_list.reverse()
#
# # print(card_list)
# while True:
#     if len(card_list) == 1:
#         break
#     card_list = card_list[:-1]
#     card_list.insert(0, card_list.pop())
#
# print(card_list[-1])

import sys
from collections import deque
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
card_deque = deque(int(i+1) for i in range(N))

while True:
    if len(card_deque) == 1:
        break

    card_deque.popleft()
    card_deque.rotate(-1)

print(card_deque[-1])



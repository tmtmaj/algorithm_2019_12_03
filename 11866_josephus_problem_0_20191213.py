
import sys
from collections import deque
cmd = lambda: sys.stdin.readline()

N, K = map(int, cmd().strip().split())
Queue = deque(int(i+1) for i in range(N))
out_list = []

while True:
    if len(Queue) == 0:
        break
    Queue.rotate(-K+1)
    out_list.append(Queue.popleft())


print("<" + ", ".join(map(str, out_list))+ ">", end="")
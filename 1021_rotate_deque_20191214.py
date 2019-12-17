import sys
from collections import deque
cmd = lambda: sys.stdin.readline()

N, M = map(int, cmd().strip().split())
target = list(map(int, cmd().strip().split()))
Deque = deque(range(1,N+1))
rotate_cnt = 0

for i in range(M):
    tar_len = Deque.index(target[i])
    if tar_len <= (len(Deque)-tar_len):
        Deque.rotate(-tar_len)
        rotate_cnt += tar_len
    else:
        Deque.rotate((len(Deque)-tar_len))
        rotate_cnt += (len(Deque)-tar_len)
    Deque.popleft()

print(rotate_cnt)


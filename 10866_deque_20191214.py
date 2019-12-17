import sys
from collections import deque

cmd = lambda: sys.stdin.readline()
N = int(cmd().strip())
Deque = deque()

for _ in range(N):
    in_ = cmd().strip().split()
    if in_[0] == "push_back":
        Deque.append(in_[1])
    elif in_[0] == "push_front":
        Deque.appendleft(in_[1])
    elif in_[0] == "front":
        if Deque:
            print(Deque[0])
        else:
            print(-1)
    elif in_[0] == "back":
        if Deque:
            print(Deque[-1])
        else:
            print(-1)
    elif in_[0] == "size":
        print(len(Deque))
    elif in_[0] == "empty":
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif in_[0] == "pop_front":
        if Deque:
            print(Deque.popleft())
        else:
            print(-1)
    elif in_[0] == "pop_back":
        if Deque:
            print(Deque.pop())
        else:
            print(-1)
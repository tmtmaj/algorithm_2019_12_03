##https://www.acmicpc.net/board/view/25456
import sys
from collections import deque

cmd = lambda: sys.stdin.readline()

trial = int(cmd().strip())
result = []

for _ in range(trial):
    in_ = cmd().strip()
    len_seq = int(cmd().strip())
    Error = False
    seq = cmd().strip()[1:-1]

    if in_.count("D") <= len_seq:
        if len(seq) != 0:
            seq = deque(map(int, seq.split(",")))
        else:
            seq = []
    else:
        Error = True
        pass

    left = True

    if not Error:
        for i in in_:
            if i == "R":
                left = not left
            elif i == "D" and left:
                seq.popleft()
            elif i == "D" and (not left):
                seq.pop()
            # print(seq)



    if Error:
        # result.append("error")
        print("error")
    else:
        # result.append(seq)
        if left:
            seq = seq
        else:
            seq.reverse()
        # result.append(list(seq))
        print("[" + ",".join(map(str, list(seq)))+"]")

# for i in result:
#     print(i)


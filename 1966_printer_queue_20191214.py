import sys
from collections import deque
cmd = lambda: sys.stdin.readline()

trial = int(cmd().strip())
result_list = []

for _ in range(trial):
    N, M = map(int, cmd().strip().split())
    Queue = deque([[i, j] for i,j in enumerate(map(int, cmd().strip().split()))])
    Target_value = Queue[M][1]
    print_cnt = 0
    # print(Target_value)
    while True:
        max_item = max(Queue, key = lambda x:x[1])
        # print(max_item[1])
        # if max_item[1] == Target_value:
        #     pass
        # else:
        Queue.rotate(-Queue.index(max_item))
        Queue.popleft()
        print_cnt += 1
        # print(Queue)
        if len(Queue) == 0 or max_item[0] == M :
            break
    # result_list.append(print_cnt)
    print(print_cnt)

# for result in result_list:
#     print(result)

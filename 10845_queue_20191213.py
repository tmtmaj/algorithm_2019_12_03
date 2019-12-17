import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())

queue = []

for _ in range(N):
    input = cmd().strip()
    if input.count("push"):
        queue.insert(0, input.split()[1])
    elif input.count("pop"):
        try:
            print(queue.pop())
        except:
            print(-1)
    elif input.count("size"):
        print(len(queue))
    elif input.count("empty"):
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input.count("front"):
        try:
            print(queue[-1])
        except:
            print(-1)
    elif input.count("back"):
        try:
            print(queue[0])
        except:
            print(-1)
import sys

trials = int(sys.stdin.readline().strip())
# trials = int(trials)
stack = []

for _ in range(trials):
    cmd = sys.stdin.readline().strip().split()
    order = cmd[0]

    if order == "push":
        stack.append(cmd[1])
    elif order == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif order == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print("-1")
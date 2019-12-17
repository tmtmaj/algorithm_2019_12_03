import sys
cmd = lambda:sys.stdin.readline()

while True:

    trial = cmd().strip()
    if trial == "0":
        break

    n, h = trial.split(maxsplit=1)
    h_list = list(map(int, h.split())) +[0]

    max_area = 0
    h_stack = []
    for i, h in enumerate(h_list):
        while h_stack and h_list[h_stack[-1]]>h:
            ih = h_list[h_stack.pop()]

            w = i - h_stack[-1] -1 if h_stack else i

            max_area = max(max_area, ih*w)

        h_stack.append(i)

    print(max_area)


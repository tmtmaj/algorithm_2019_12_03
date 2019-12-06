import sys
trials = int(sys.stdin.readline().strip())

stack = []
answer = []
for trial in range(0, trials):
    input_PS = sys.stdin.readline().strip()
    Error_code = False
    for piece in input_PS:
        if piece == "(":
            stack.append(piece)
        elif piece == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                Error_code = True


    if len(stack) == 0:
        if Error_code == False:
            answer.append("YES")

        else:
            answer.append("NO")
    else:
        answer.append("NO")
    stack.clear()

for ans in answer:
    print(ans)


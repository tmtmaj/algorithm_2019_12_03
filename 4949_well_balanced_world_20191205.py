import sys
# trials = int(sys.stdin.readline().strip())
cmd = ""
answers = []
Conti = True

while Conti:
    cmd = sys.stdin.readline()
    # print(cmd)
    stack = []
    Error = False
    if cmd == ".\n":
        # print(cmd)
        Conti = False
    elif cmd == " .\n":
        Error = False
    else:
        for char in cmd:
            if char == "(" or char == "[":
                stack.append(char)
            elif char == ")" and len(stack) != 0:
                if stack[-1] == "[":
                    Error = True
                else:
                    stack.pop()
            elif char == "]" and len(stack) != 0:
                # print("yeah2")
                if stack[-1] == "(":
                    # print("yeah3")
                    Error = True
                else:
                    stack.pop()
            elif (char == "]" or char == ")") and len(stack) == 0:
                Error = True

    if Conti:
        if Error == True or len(stack) != 0:
            answers.append("no")
        else:
            # print("yeah")
            answers.append("yes")

for answer in answers:
    print(answer)
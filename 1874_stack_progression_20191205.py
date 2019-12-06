import sys

# def empty(lst):
#     if len(lst) == 0:
#         return True
#     else:
#         return False
#
# trails = int(sys.stdin.readline().strip())
# stack = []
# ori_stack = [int(i) for i in range(1, trails+1)][::-1]
# # print(ori_stack)
# Failed = False
# answers = []
#
# for _ in range(trails):
#     cmd = int(sys.stdin.readline().strip())
#     if len(stack) == 0:
#         while not empty(ori_stack):
#             stack.append(ori_stack.pop())
#             answers.append("+")
#             if not empty(ori_stack) and ori_stack[-1] == cmd :
#                 answers.append("+")
#                 answers.append("-")
#                 ori_stack.pop()
#                 break
#     elif cmd == stack[-1]:
#         stack.pop()
#         answers.append("-")
#     else:
#         if empty(ori_stack):
#             Failed = True
#             #break
#         else:
#             while not empty(ori_stack):
#                 # print("yeah")
#                 stack.append(ori_stack.pop())
#                 answers.append("+")
#                 if not empty(ori_stack) and ori_stack[-1] == (cmd):
#                     answers.append("+")
#                     answers.append("-")
#                     ori_stack.pop()
#                     break
#     # print(stack)
#
# if Failed == True:
#     print("NO")
# else:
#     for answer in answers:
#         print(answer)

# trails = int(sys.stdin.readline().strip())

cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
cnt = 1
stack = []
answers = []
no_flag = False

for n in range(N):
    num = int(cmd().strip())
    while num >= cnt:
        stack.append(cnt)
        cnt += 1
        answers.append("+")
    if stack[-1] == num:
        stack.pop()
        answers.append("-")
    else:
        no_flag = True

if no_flag:
    print("NO")
else:
    for answer in answers:
        print(answer)
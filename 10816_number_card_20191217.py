import sys
cmd = lambda: sys.stdin.readline()

N = cmd()
N_list = list(map(int, cmd().strip().split()))
M = cmd()
M_list = list(map(int, cmd().strip().split()))

# N_set = set(N_list)
N_list_dict = {}
for i in N_list:
    N_list_dict[i] = N_list.count(i)
# N_list = list(N_set)
# N_list.sort()
result = []
# print(N_list, N_list_dict)

# def find_card(card):
#     left = 0
#     right = len(N_list)
#
#     while True:
#
#         if card < N_list[left] or card > N_list[right-1]:
#             result.append("0")
#             break
#
#         mid = (left+right)//2
#
#         if mid == left and card != N_list[mid]:
#             result.append("0")
#             break
#
#         if card > N_list[mid]:
#             left = mid
#         elif card < N_list[mid]:
#             right = mid
#         else:
#             result.append(N_list_dict[card])
#             break

for m in M_list:
    try:
        result.append(N_list_dict[m])
    except:
        result.append(0)

for r in result:
    print(r, end=" ")



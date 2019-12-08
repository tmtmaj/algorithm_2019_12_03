import sys

cmd = lambda: sys.stdin.readline()

plus_list = cmd().strip().split("-")
SUM = 0

# print(plus_list)

if plus_list[0] == "":
    SUM -= sum(list(map(int, plus_list[1].split("+"))))
    plus_list = plus_list[2:]
else:
    SUM += sum(list(map(int, plus_list[0].split("+"))))
    plus_list = plus_list[1:]

for plus_line in plus_list:
    SUM -= sum(list(map(int, plus_line.split("+"))))



print(SUM)

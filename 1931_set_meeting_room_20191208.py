import sys

cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
meeting_list = []

for _ in range(N):
    meeting_list.append(list(map(int, cmd().strip().split())))

meeting_list.sort(key = lambda meeting_list: meeting_list[0])
meeting_list.sort(key = lambda meeting_list: meeting_list[1])
end_time = 0
cnt = 0
# answers = []

for start, end in meeting_list:
    if start >= end_time:
        cnt += 1
        # answers.append([start, end])
        end_time = end

print(cnt)

# sort 정렬시 순서를 정렬할 index들의 순서를 정할 수 있다.
# a = [[1,1], [2,4], [3,3], [4,4],[1,2], [3,4]]
#
# print(a)
#
# a.sort(key= lambda x : [x[1], x[0]])
#
# print(a)
#
# a.sort(key= lambda x : [x[0], x[1]])
#
# print(a)
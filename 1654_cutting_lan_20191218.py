import sys

cmd = lambda: sys.stdin.readline()

K, N = map(int, cmd().strip().split())
lan_list =[]

for _ in range(K):
    lan_list.append(int(cmd().strip()))

lan_list.sort(reverse=True)

# print(K, N, lan_list)


min = 0
max = lan_list[0]
output = 1

while max >= min:
    mid = (min + max)//2
    cnt = 0
    if mid == 0:
        output = 1
        break

    for lan in lan_list:
        cnt += lan//mid
        if cnt >= N and mid > output:
            output = mid
            break

    if cnt >= N:
        min = mid + 1
    else:
        max = mid - 1

print(output)

# def solution(k,n, arr):
#     high = arr[0]
#     low = 0
#     result = 0
#
#     while low <= high:
#         mid = (high + low) // 2
#         cnt = 0
#         if mid == 0: return 1
#         for val in arr:
#             cnt += val//mid
#             if cnt >= n and mid > result:
#                 result = mid
#                 break
#
#         if cnt < n:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return  result
#
# if __name__ == "__main__":
#     K, N = map(int,input().split())
#     arr = []
#
#     for _ in range(K):
#         arr.append(int(input()))
#     arr.sort(reverse = True)
#
#     print(solution(K, N, arr))

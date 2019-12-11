import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())
stairs = []

for _ in range(N):
    stairs.append(int(cmd().strip()))

rewards = [stairs[0], stairs[0]+stairs[1], max(stairs[1]+stairs[2], stairs[0]+stairs[2])]

# print(rewards)
for n in range(3,N):
    rewards.append(max(stairs[n]+stairs[n-1]+rewards[n-3], stairs[n]+rewards[n-2]))

print(rewards[-1])
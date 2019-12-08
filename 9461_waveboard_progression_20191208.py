import sys
cmd = lambda: sys.stdin.readline()

N = int(cmd().strip())

wb_lists = [1,1,1,2,2,3,4,5,7,9]
Trials = []

for _ in range(N):
    Trial = int(cmd().strip())
    if Trial > len(wb_lists)-1:
        for n in range((len(wb_lists)-1), Trial):
            wb_lists.append(wb_lists[n] + wb_lists[n-4])
    Trials.append(Trial)

for Trial in Trials:
    print(wb_lists[Trial-1])

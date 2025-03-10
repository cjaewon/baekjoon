import sys

N, T = map(int, input().split())
timetable = [0 for i in range(100001)]

for i in range(N):
  K = int(sys.stdin.readline().rstrip())

  for j in range(K):
    S, E = map(int, sys.stdin.readline().rstrip().split())

    timetable[S] += 1
    timetable[E] -= 1

for i in range(1, 100001):
  timetable[i] += timetable[i - 1]

i = 0
time_satisfaction = sum(timetable[0:T+1])
max_time_satisfaction = time_satisfaction
max_time_satisfaction_pos = (0, T)

# window start : i, window end : i + T
while i < 100001 - T - 1:
  if max_time_satisfaction < time_satisfaction:
    max_time_satisfaction = time_satisfaction
    max_time_satisfaction_pos = (i + 1, i + T + 1)

  time_satisfaction -= timetable[i + 1]
  time_satisfaction += timetable[i + T + 1]

  i += 1

print(max_time_satisfaction_pos[0], max_time_satisfaction_pos[1])
import sys

N, K = map(int, input().split())

rank = [sys.stdin.readline().rstrip() for i in range(N)]
name_count = [0 for i in range(21)]
good_friend = 0

if N == K:
  K -= 1

for i in range(1, K + 1):
  name_count[len(rank[i])] += 1

for i in range(N - 1):
  good_friend += name_count[len(rank[i])]

  name_count[len(rank[i + 1])] -= 1

  if i + K + 1 < len(rank):
    name_count[len(rank[i + K + 1])] += 1

print(good_friend)
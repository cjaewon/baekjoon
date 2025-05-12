import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
indeg = [0 for i in range(N + 1)]

for i in range(M):
  A, B = map(int, input().split())

  graph[A].append(B)
  indeg[B] += 1
  # A -> B

q = deque([v for v in range(1, N + 1) if indeg[v] == 0])
dp = [1 for i in range(N + 1)]

while q:
  v = q.popleft()

  for adj_v in graph[v]:
    indeg[adj_v] -= 1

    if indeg[adj_v] == 0:
      q.append(adj_v)
      dp[adj_v] = dp[v] + 1

for i in range(1, N + 1):
  print(dp[i], end=" ")

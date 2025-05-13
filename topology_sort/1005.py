import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def main():

  N, K = map(int, input().split())
  build_time = [0] + list(map(int, input().split()))

  graph = [[] for i in range(N + 1)]
  indeg = [0 for i in range(N + 1)]

  for i in range(K):
    X, Y = map(int, input().split())
    # X -> Y

    graph[X].append(Y)
    indeg[Y] += 1

  W = int(input())

  q = deque([v for v in range(1, N + 1) if indeg[v] == 0])
  dp = [0 for i in range(N + 1)]

  for v in q:
    dp[v] = build_time[v]

  while q:
    v = q.popleft()

    for adj_v in graph[v]:
      indeg[adj_v] -= 1
      dp[adj_v] = max(dp[adj_v], dp[v] + build_time[adj_v])

      if indeg[adj_v] == 0:
        q.append(adj_v)

  print(dp[W])

for i in range(int(input())):
  main()
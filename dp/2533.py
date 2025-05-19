"""
tree 에서의 dp

점화식 :
  dp[vertex][0] = 현재 정점이 얼리 어답터가 아닐 때 정점을 포함한 sub-tree의 최소 얼리 어답터의 수
  dp[vertex][1] = 현재 정점이 얼리 어답터 일 때 정점을 포함한 sub-tree의 최소 얼리 어답터의 수
 
  dp[vertex][0] = dp[child_v1][1] + dp[child_v2][1] + ...
  dp[vertex][1] = 1 + min(dp[child_v1][0], dp[child_v1][1]) + ...

  dfs로 내려갔다가 다시 올라오면서 점화식 채우기

답 : 
  min(dp[root][0], dp[root][1])
"""

import sys

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for i in range(N + 1)]

dp = [[0, 0] for i in range(N + 1)]

for _ in range(N - 1):
  u, v = map(int, input().split())
  
  graph[u].append(v)
  graph[v].append(u)

root = 1
visited = set()

def dfs(v):
  visited.add(v)

  for adj_v in graph[v]:
    if adj_v not in visited:
      dfs(adj_v)

      dp[v][0] += dp[adj_v][1]
      dp[v][1] += min(dp[adj_v])
      
  dp[v][1] += 1

dfs(root)

print(min(dp[root]))
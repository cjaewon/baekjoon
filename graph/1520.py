import sys

sys.setrecursionlimit(100000)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(m)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
memo = [[-1 for j in range(n)] for i in range(m)]

def dfs(y, x, l):
  if y == m - 1 and x == n - 1:
    return 1
  if memo[y][x] != -1:
    return memo[y][x]

  memo[y][x] = 0

  for i in range(4):
    if 0 <= y + dy[i] <= m - 1 and 0 <= x + dx[i] <= n - 1:
      if graph[y + dy[i]][x + dx[i]] < l:
        memo[y][x] += dfs(y + dy[i], x + dx[i], graph[y + dy[i]][x + dx[i]])

  return memo[y][x]

print(dfs(0, 0, graph[0][0]))
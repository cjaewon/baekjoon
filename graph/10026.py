import sys

sys.setrecursionlimit(100000)

n = int(input())
graph = [list(input()) for i in range(n)]
visited = [[0 for j in range(n)] for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count1 = 0
count2 = 0

def dfs(y, x, t):
  visited[y][x] = 1

  for i in range(4):
    if 0 <= y + dy[i] <= n - 1 and 0 <= x + dx[i] <= n - 1:
      if graph[y + dy[i]][x + dx[i]] in t and not visited[y + dy[i]][x + dx[i]]:
        dfs(y + dy[i], x + dx[i], t)

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      dfs(i, j, [graph[i][j]])
      count1 += 1

visited = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      if graph[i][j] == "G" or graph[i][j] == "R":
        dfs(i, j, ["G", "R"])
      else:
        dfs(i, j, ["B"])
      count2 += 1

print(count1, count2)
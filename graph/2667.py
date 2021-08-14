n = int(input())
graph = [list(map(int, list(input()))) for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0
result = []

def dfs(y, x):
  global count

  graph[y][x] = 0
  count += 1

  for i in range(4):
    if 0 <= y + dy[i] <= n - 1 and 0 <= x + dx[i] <= n - 1:
      if graph[y + dy[i]][x + dx[i]] == 1:
        dfs(y + dy[i], x + dx[i])

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      count = 0
      dfs(i, j)

      result.append(count)

print(len(result))
print("\n".join(map(str, sorted(result))))
N, M = map(int, input().split())
grid = [list(input()) for i in range(N)]

visited = set()

def dfs(y, x, parent, dist):
  visited.add((y, x))

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    if 0 <= y + dy < N and 0 <= x + dx < M and grid[y + dy][x + dx] == grid[y][x]:
      if (y + dy, x + dx) not in visited:
        dfs(y + dy, x + dx, (y, x), dist + 1)
      else:
        if parent != None and (y + dy, x + dx) != parent and dist >= 4:
          print("Yes")
          exit()


for y in range(N):
  for x in range(M):
    if (y, x) not in visited:
      dfs(y, x, None, 1)

print("No")
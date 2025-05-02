N, M = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

visited = set()

def dfs_candidate_check(y: int, x: int, height: int, comp: list[(int, int)]):
  visited.add((y, x))
  comp.append((y, x))

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
    if 0 <= y + dy < N and 0 <= x + dx < M and (y + dy, x + dx) not in visited and grid[y + dy][x + dx] == height:
      dfs_candidate_check(y + dy, x + dx, height, comp)

comps = []

for i in range(N):
  for j in range(M):
    if (i, j) not in visited:
      comp = []
      dfs_candidate_check(i, j, grid[i][j], comp)

      if comp:
        comps.append(comp)

top_cnt = 0

for comp in comps:
  is_top = True

  for y, x in comp:
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
      if 0 <= y + dy < N and 0 <= x + dx < M and grid[y + dy][x + dx] > grid[y][x]:
        is_top = False
        break

    if not is_top:
      break

  if is_top:
    top_cnt += 1

print(top_cnt)
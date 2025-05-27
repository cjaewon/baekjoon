import sys

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

visited: set[tuple[int, int]] = set()
safe_zone_cnt = 0

def dfs(y: int, x: int, rec_visited: set[tuple[int, int]]):
  global safe_zone_cnt

  visited.add((y, x))
  rec_visited.add((y, x))

  dy, dx = 0, 0

  match grid[y][x]:
    case "U":
      dy -= 1
    case "D":
      dy += 1
    case "R":
      dx += 1
    case "L":
      dx -= 1


  if 0 <= dy + y < N and 0 <= dx + x < M:
    if (y + dy, x + dx) in rec_visited:
      safe_zone_cnt += 1

    if (y + dy, x + dx) not in visited:
      dfs(y + dy, x + dx, rec_visited)
  else:
    safe_zone_cnt += 1

  rec_visited.remove((y, x))


for y in range(N):
  for x in range(M):
    if (y, x) not in visited:
      dfs(y, x, set())
  
print(safe_zone_cnt)
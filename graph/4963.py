from collections import deque

while True:
  w, h = map(int, input().split())
  
  if w == 0 and h == 0:
    break

  grid = [list(map(int, input().split())) for i in range(h)]

  visited = set()
  area_cnt = 0

  for i in range(h):
    for j in range(w):
      if (i, j) in visited:
        continue
      if grid[i][j] == 0:
        continue

      area_cnt += 1

      q = deque([(i, j)])
      visited.add((i, j))

      while q:
        y, x = q.popleft()

        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
          if 0 <= y + dy < h and 0 <= x + dx < w and grid[y + dy][x + dx] == 1 and (y + dy, x + dx) not in visited:
            visited.add((y + dy, x + dx))
            q.append((y + dy, x + dx))
  
  print(area_cnt)
from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]

max_area_cnt = 0

# 차피 100 일 때는 모두 잠기니 영역이 없을 것임.
for k in range(0, 100):
  visited = set()
  area_cnt = 0

  for i in range(N):
    for j in range(N):
      if (i, j) in visited: continue
      if grid[i][j] <= k: continue

      area_cnt += 1

      visited.add((i, j))
      queue = deque([(i, j)])


      while queue:
        y, x = queue.popleft()
        
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
          if 0 <= y + dy < N and 0 <= x + dx < N and grid[y + dy][x + dx] > k and (y + dy, x + dx) not in visited:
            visited.add((y + dy, x + dx))
            queue.append((y + dy, x + dx))
  max_area_cnt = max(max_area_cnt, area_cnt)
print(max_area_cnt)


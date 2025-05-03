from collections import deque

grid = [list(map(int, input().split())) for i in range(5)]
r, c = map(int, input().split())

# 답을 내는 것이 가능한지 먼저 체크
# 가능하다면 => 다음 로직
# 불가능하다면 => -1 출력

q = deque([(r, c)])
visited = set()

while q:
  y, x = q.popleft()

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    if 0 <= y + dy < 5 and 0 <= x + dx < 5 and (y + dy, x + dx) not in visited and grid[y + dy][x + dx] != -1:
      visited.add((y + dy, x + dx))
      q.append((y + dy, x + dx))

for i in range(5):
  for j in range(5):
    if grid[i][j] not in (-1, 0):
      if (i, j) not in visited:
        print(-1)
        exit()
      


# 답을 내는게 가능하므로 다음 로직 실행

q = deque([(r, c, 0, [True] + [False] * 6)]) # y, x, dist(time), num_pos
visited = set()

while q:
  y, x, dist, num_pos_checked  = q.popleft()

  if grid[y][x] != 0:
    num_pos_checked[grid[y][x]] = True

  if all(num_pos_checked):
    print(dist)
    break

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    if 0 <= y + dy < 5 and 0 <= x + dx < 5 and grid[y + dy][x + dx] != -1 and (y + dy, x + dx, "".join(map(str, num_pos_checked))) not in visited:
      visited.add((y + dy, x + dx, "".join(map(str, num_pos_checked))))
      q.append((y + dy, x + dx, dist + 1, num_pos_checked.copy()))
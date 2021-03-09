from collections import deque

m, n = map(int, input().split(' '))
table = [list(map(int, input().split(' '))) for i in range(n)]


q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ripe_tomatoes = 0

for i in range(n):
  for j in range(m):
    if table[i][j] == 1:
      ripe_tomatoes += 1
      q.append((i, j, 0)) # TIL: bfs에서 두 지점에 시작하면 두 지점 모두 먼저 큐에 넣어준다.
    elif table[i][j] == -1:
      ripe_tomatoes += 1

if ripe_tomatoes == n * m:
  print(0)
  exit()

day = 0

while True:
  e = q.popleft()

  for i in range(4):
    y = e[0] + dy[i]
    x = e[1] + dx[i]

    if y <= n -1 and y >= 0 and x <= m - 1 and x >= 0 and table[y][x] == 0:
      table[y][x] = 1
      q.append((y, x, e[2] + 1))

  if not q:
    day = e[2]
    break

for i in range(n):
  for j in range(m):
    if table[i][j] == 0:
      print(-1)
      exit()

print(day)
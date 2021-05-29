"""
반복문 while을 True로 했기 때문에 q가 비어있을때도 실행이 되서 런타임에러(IndexError)가 떳다
while q: 로 바꿔 제출하여 해결했다.
"""

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
      q.append((i, j, 0))
    elif table[i][j] == -1:
      ripe_tomatoes += 1

if ripe_tomatoes == n * m:
  print(0)
  exit()

day = 0

while q:
  e = q.popleft()

  for i in range(4):
    y = e[0] + dy[i]
    x = e[1] + dx[i]

    if 0 <= y <= n - 1 and 0 <= x <= m - 1 and table[y][x] == 0:
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
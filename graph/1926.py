from collections import deque

c = []

def bfs(table, i, j, n, m):
  dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
  q = deque()
  count = 0

  q.append((i, j))
  table[i][j] = 0

  while True:
    e = q.popleft()
    count += 1

    for i in range(4):
      if e[0] + dy[i] <= n - 1 and e[0] + dy[i] >= 0 and e[1] + dx[i] <= m - 1 and e[1] + dx[i] >= 0 and table[e[0] + dy[i]][e[1] +dx[i]] == 1:
        table[e[0] + dy[i]][e[1] +dx[i]] = 0
        q.append((e[0] + dy[i], e[1] + dx[i]))

    if not q:
      c.append(count)
      break

if __name__ == "__main__":
  n, m = map(int, input().split(' '))
  table = [0 for i in range(n)]

  for i in range(n):
    table[i] = list(map(int, input().split(' ')))

  for i in range(n):
    for j in range(m):
      if table[i][j] == 1:
        bfs(table, i, j, n, m)

  print(len(c))
  print(0 if len(c) == 0 else max(c)) # TIL: max(c), len(c) == 0 이면 RuntimeError (ValueError)가 난다.
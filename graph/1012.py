import queue

def bfs(table, y, x, m, n):
  q = queue.Queue()

  q.put((y, x))
  table[y][x] = 0

  while not q.empty():
    e = q.get()
    fy, fx = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(4):
      if e[0] + fy[i] <= n - 1 and e[0] + fy[i] >= 0 and  e[1] + fx[i] <= m - 1 and e[1] + fx[i] >= 0:
        if table[e[0] + fy[i]][e[1] + fx[i]] == 1:
          table[e[0] + fy[i]][e[1] + fx[i]] = 0
          q.put((e[0] + fy[i], e[1] + fx[i]))

def solve():
  count = 0
  m, n, c = map(int, input().split(' '))
  table = [[0 for i in range(m)] for j in range(n)]

  for _ in range(c):
    x, y = map(int, input().split(' '))
    table[y][x] = 1

  for y in range(n):
    for x in range(m):
      if table[y][x] == 1:
        bfs(table, y, x, m, n)
        count += 1
        
  print(count)

n = int(input())

for i in range(n):
  solve()
from collections import deque

n, m = map(int, input().split())
graph = [[0 for i in range(n)] for i in range(n)]
used = []

if n <= m:
  for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = graph[b - 1][a - 1] =  1
else:
  for i in range(n):
    if i < m:
      a, b = map(int, input().split())
      graph[a - 1][b - 1] = graph[b - 1][a - 1] =  1
      used.append(a - 1)
      used.append(b - 1)

for i in range(n):
  if not i in used:
    graph[i][i] = 1


q = deque()

def bfs(i, j):
  q.append((i, j))
  q.append((j, i))

  while len(q) > 0:
    i, j = q.popleft()
    graph[i][j] = 0
    graph[j][i] = 0

    for k in range(n):
      if graph[i][k] == 1:
        graph[k][i] = 0
        graph[i][k] = 0
        q.append((k, i)) 

count = 0
    
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(i, j)
      count += 1
      break

print(count)
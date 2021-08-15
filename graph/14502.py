import copy
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
temp = []
result = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
startpoints = []

q = deque()

def bfs():
  count = 0

  while q:
    y, x = q.popleft()

    for i in range(4):
      if 0 <= y + dy[i] <= n - 1 and 0 <= x + dx[i] <= m - 1:
        if temp[y + dy[i]][x + dx[i]] == 0:
          temp[y + dy[i]][x + dx[i]] = 2
          q.append((y + dy[i], x + dx[i]))

  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        count += 1

  return count

for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      startpoints.append((i, j))

for i1 in range(n):
  for j1 in range(m):
    if graph[i1][j1] == 0:
      for i2 in range(n):
        for j2 in range(m):
          if graph[i2][j2] == 0 and (i2, j2) != (i1, j1):
            for i3 in range(n):
              for j3 in range(m):
                if graph[i3][j3] == 0 and (i3, j3) != (i1, j1) and (i3, j3) != (i2, j2):
                  temp = copy.deepcopy(graph)
                  q = deque(startpoints)

                  temp[i3][j3] = 1
                  temp[i2][j2] = 1
                  temp[i1][j1] = 1

                  result.append(bfs())
if len(result) == 0:
  print(0)
else:
  print(max(result))
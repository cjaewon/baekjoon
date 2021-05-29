from collections import deque

n, m = map(int, input().split())
graph = [[0 for i in range(n)] for i in range(n)]
result = []

for i in range(m):
  a, b = map(int, input().split())
  graph[a - 1][b - 1] = 1
  graph[b - 1][a - 1] = 1

for i in range(n):
  q = deque()

  q.append((i, 0))
  s = 0
  visited = [0 for i in range(n)]

  while True:
    curr, cost = q.popleft()

    if sum(visited) == n:
      break

    for j in range(n):
      if graph[curr][j] == 1 and visited[j] == 0:
        s += cost
        visited[j] = 1
        q.append((j, cost + 1))


  result.append((i + 1, s))

print(min(result, key=lambda n: n[1])[0])
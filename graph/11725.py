from collections import deque
import sys

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

q = deque()
root_nodes = []

for i in range(n - 1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a - 1][b - 1] = 1
  graph[b - 1][a - 1] = 1

  if a == 1:
    root_nodes.append(b - 1)
  elif b == 1:
    root_nodes.append(a - 1)

for node in root_nodes:
  q.append((node, 0))

count = 0
currdep = 0

while q:
  node, dep = q.popleft()
  count += 1

  print(q)

  if currdep != dep:
    print(count)

    currdep = dep
    count = 0

  for i in range(0, n):
    if graph[node][i] == 1:
      q.append((node, dep + 1))

      graph[node][i] = 0
      graph[i][node] = 0
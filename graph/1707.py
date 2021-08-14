import sys

sys.setrecursionlimit(100000)

t = int(input())
graph = [[] for i in range(20001)]
visited = [0 for i in range(20001)]

result = "YES"

def dfs(k, t):
  global result

  for v in graph[k]:
    if t == 1:
      if visited[v] == 1:
        result = "NO"
        return
      elif visited[v] == 2:
        continue

      visited[v] = 2
      dfs(v, 2)
    else:
      if visited[v] == 2:
        result = "NO"
        return
      elif visited[v] == 1:
        continue 

      visited[v] = 1
      dfs(v, 1)

for i in range(t):
  k, v = map(int, input().split())
  last = 0
  graph = [[] for i in range(20001)]
  visited = [0 for i in range(20001)]
  startpoint = []

  result = "YES"

  for j in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    startpoint.append(a)

  for p in startpoint:
    if visited[p] == 0:
      visited[last] = 1
      dfs(p, 1)

  print(result)
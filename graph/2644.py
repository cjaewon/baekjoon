import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

def dfs(v, dest, path: int):
  if v == dest:
    return path

  visited.add(v)

  for adj_v in graph[v]:
    if adj_v not in visited:
      r = dfs(adj_v, dest, path + 1)

      if r != -1:
        return r
      
  return -1
n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = defaultdict(list)

for i in range(m):
  x, y = map(int, input().split())

  graph[y].append(x)
  graph[x].append(y)

visited = set()

r = dfs(a, b, 0)
print(r)


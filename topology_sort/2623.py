import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)
# graph[a] -> [b, c, d]

for i in range(M):
  order = list(map(int, input().split()))
  
  for k in range(1, len(order) - 1):
    if order[k + 1] in graph[order[k]]:
      continue

    graph[order[k]].append(order[k + 1])

visited = set()
rec_stack = set()
tp_sort = []

def dfs(v):
  # print(v, "dfs!dfs!")
  visited.add(v)
  rec_stack.add(v)

  for adj_v in graph[v]:
    if adj_v in rec_stack:
      print(0)
      exit()
    if adj_v in visited:
      continue
    
    dfs(adj_v)

  rec_stack.remove(v)
  tp_sort.append(v)

for v in range(1, N + 1):
  if v not in visited:
    dfs(v)

tp_sort.reverse()

for v in tp_sort:
  print(v)

print(graph)
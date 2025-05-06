import sys
from collections import defaultdict

sys.setrecursionlimit(10000000)  

N, M = map(int, input().split())

graph = defaultdict(list)
visited = [False for i in range(32001)]

topology_sort = []

for i in range(M):
  A, B = map(int, sys.stdin.readline().rstrip().split())
  # B -> A

  graph[B].append(A)

def dfs(k):
  visited[k] = True
  
  for adj_node in graph[k]:
    if not visited[adj_node]:
      dfs(adj_node)

  topology_sort.append(k)


for i in range(1, N + 1):
  if not visited[i]:
    dfs(i)

for k in topology_sort:
  print(k, end=" ")
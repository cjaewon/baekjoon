import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10 ** 5)

input = lambda: sys.stdin.readline().rstrip()
print = sys.stdout.write

N = int(input())
root = 1

graph = defaultdict(list)

for i in range(N - 1):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)

K = math.floor(math.log2(N))

parent = [[0 for j in range(K + 1)] for i in range(N + 1)]
depth = [0 for i in range(N + 1)]

visited = set()

def dfs(v, curr_dep):
  visited.add(v)
  depth[v] = curr_dep

  for adj_v in graph[v]:
    if adj_v not in visited:
      parent[adj_v][0] = v
      dfs(adj_v, curr_dep + 1)  

dfs(root, 1)

for i in range(1, K + 1):
  for v in range(1, N + 1):
    parent[v][i] = parent[parent[v][i - 1]][i - 1]

M = int(input())

for i in range(M):
  a, b = map(int, input().split())

  if depth[a] > depth[b]:
    a, b = b, a

  diff = depth[b] - depth[a]

  for i in range(0, K + 1):
    if diff & (1 << i):
      b = parent[b][i]

  if a == b:
    lca = a
  else:
    for i in range(K, -1, -1):
      if parent[a][i] != parent[b][i]:
        a = parent[a][i]
        b = parent[b][i]
    
    lca = parent[a][0]

  print(str(lca) + "\n")
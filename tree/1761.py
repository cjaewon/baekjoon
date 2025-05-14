import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = defaultdict(list)

for i in range(N - 1):
  a, b, d = map(int, input().split())
  
  graph[a].append((b, d))
  graph[b].append((a, d))
  
# 임의로 루트를 1로 설정.
# dfs를 통해 실행 도중 각 정점들을 깊이, dist, parent table 처리 

K = math.floor(math.log2(N))

depth = [0 for i in range(N + 1)]
parent = [[0 for i in range(K + 1)] for i in range(N + 1)]
dist = [0 for i in range(N + 1)]

def dfs(v, curr_dep, curr_dist, visited=set()):
  visited.add(v)
  depth[v] = curr_dep
  dist[v] = curr_dist

  for adj_v, edge_d in graph[v]:
    if adj_v not in visited:
      parent[adj_v][0] = v
      dfs(adj_v, curr_dep + 1, curr_dist + edge_d, visited)

dfs(1, 0, 0)

# LCA with binary lifting

# dp with parent table
for i in range(1, K + 1):
  for v in range(1, N + 1):
    parent[v][i] = parent[parent[v][i - 1]][i - 1]

M = int(input())

for i in range(M):
  fa, fb = map(int, input().split())
  a, b = fa, fb

  if depth[a] < depth[b]:
    a, b = b, a

  diff = depth[a] - depth[b]

  for i in range(0, K + 1):
    if diff & (1 << i):
      a = parent[a][i]

  if a == b:
    lca = a  
  else:
    for i in range(K, -1, -1):
      if parent[a][i] != parent[b][i]:
        a = parent[a][i]
        b = parent[b][i]

    lca = parent[a][0]
  
  print((dist[fa] - dist[lca]) + (dist[fb] - dist[lca]))
    
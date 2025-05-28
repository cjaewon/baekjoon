import sys
import math

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

root = 1
graph: list[list[tuple[int, int]]] = [[] for i in range(N + 1)]

for i in range(N - 1):
  u, v, w = map(int, input().split())

  graph[u].append((v, w))
  graph[v].append((u, w))

# root node로 부터 해당 노드까지의 경로의 간선의 합들을 저장하자 
weight_sum_from_root = [0 for i in range(N + 1)]

# binary lifting - sparse table def
K = math.floor(math.log2(N))
parent = [[0 for j in range(K + 1)] for i in range(N + 1)]
depth = [0 for i in range(N + 1)] 

def weight_calc_dfs(v: int, curr_w: int, curr_dep: int, visited: set[int]):
  visited.add(v)
  weight_sum_from_root[v] = curr_w
  depth[v] = curr_dep

  for adj_v, edge_w in graph[v]:
    if adj_v not in visited:
      weight_calc_dfs(adj_v, curr_w + edge_w, curr_dep + 1, visited)
      parent[adj_v][0] = v

weight_calc_dfs(root, 0, 1, visited=set())

# binary lifting - sparse table filling

for i in range(1, K + 1):
  for v in range(1, N + 1):
    parent[v][i] = parent[parent[v][i - 1]][i - 1]

M = int(input())

# binary lifting - lca calc
def calc_lca(a: int, b: int) -> int:
  if depth[a] < depth[b]:
    a, b = b, a

  diff = depth[a] - depth[b]

  for i in range(K + 1):
    if diff & (1 << i):
      a = parent[a][i]

  if a == b:
    return a
  
  for i in range(K, -1, -1):
    if parent[a][i] != parent[b][i]:
      a = parent[a][i]
      b = parent[b][i]

  return parent[a][0]

for i in range(M):
  query = list(map(int, input().split()))

  match query:
    case [1, u, v]:
      lca = calc_lca(u, v)
      w = (weight_sum_from_root[u] - weight_sum_from_root[lca]) + (weight_sum_from_root[v] - weight_sum_from_root[lca])

      print(w)
    case [2, u, v, k]:
      lca = calc_lca(u, v)

      if depth[u] - depth[lca] + 1 > k:
        k_vertex = u

        for i in range(K + 1):
          if (k - 1) & (1 << i):
            k_vertex = parent[k_vertex][i]

        print(k_vertex)
      elif depth[u] - depth[lca] + 1 < k:
        k_vertex = v

        for i in range(K + 1):
          if depth[v] - depth[lca] - (k - (depth[u] - depth[lca] + 1)) & (1 << i):
            k_vertex = parent[k_vertex][i]

        print(k_vertex)
      else:
        print(lca)


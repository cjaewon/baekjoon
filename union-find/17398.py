import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, Q = map(int, input().split())

edges = [0] + [list(map(int, input().split())) for _ in range(M)]

queries = [int(input()) for i in range(Q)]
queries_set = set(queries) 

parent = [v for v in range(N + 1)]
size = [1 for _ in range(N + 1)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]

def union(x, y):
  rx, ry = find(x), find(y)

  if rx == ry:
    return
  
  if size[rx] < size[ry]:
    rx, ry = ry, rx

  parent[ry] = rx
  size[rx] += size[ry]

for i in range(1, M + 1):
  if i not in queries_set:
    union(edges[i][0], edges[i][1])

cost = 0

for idx in reversed(queries):
  u, v = edges[idx]
  ru, rv = find(u), find(v)

  if ru == rv:
    continue
  
  cost += size[ru] * size[rv]
  union(u, v)

print(cost)
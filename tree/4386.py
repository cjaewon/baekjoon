import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

parent = {}
rank = {}

def make_set(x):
  parent[x] = x
  rank[x] = 0

  return x

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  rx, ry = find(x), find(y)

  if rx == ry:
    return
  
  if rank[rx] < rank[ry]:
    parent[rx] = ry
  else:
    parent[ry] = rx

    if rank[rx] == rank[ry]:
      rank[rx] += 1


n = int(input())
pos = [tuple(map(float, input().split())) for i in range(n)]
edges: list[tuple[float, tuple[float, float], tuple[float, float]]] = []

for i in range(len(pos)):
  x1, y1 = pos[i]
  make_set((x1, y1))

  for j in range(i, len(pos)):
    x2, y2 = pos[j]

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    edges.append((distance, (x1, y1), (x2, y2)))
    
edges.sort(reverse=True)

# Kruskal Algorithm with (Union-Find DS)

e_cnt = 0
dist_sum = 0

while e_cnt < n - 1:
  dist, (x1, y1), (x2, y2) = edges.pop() 

  if find((x1, y1)) == find((x2, y2)):
    continue

  union((x1, y1), (x2, y2))
  dist_sum += dist
  e_cnt += 1

print(f"{dist_sum:0.3}")


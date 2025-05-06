import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
pos = [tuple(map(int, input().split())) for i in range(N)]

edges = []

pos_sort_by_x = sorted(pos, key=lambda x: x[0])
pos_sort_by_y = sorted(pos, key=lambda x: x[1])
pos_sort_by_z = sorted(pos, key=lambda x: x[2])

for i in range(1, len(pos)):
  edges.append((abs(pos_sort_by_x[i][0] - pos_sort_by_x[i - 1][0]), pos_sort_by_x[i], pos_sort_by_x[i - 1]))
  edges.append((abs(pos_sort_by_y[i][1] - pos_sort_by_y[i - 1][1]), pos_sort_by_y[i], pos_sort_by_y[i - 1]))
  edges.append((abs(pos_sort_by_z[i][2] - pos_sort_by_z[i - 1][2]), pos_sort_by_z[i], pos_sort_by_z[i - 1]))

edges.sort(reverse=True)

parent = {}
rank = {}

def make_set(x):
  parent[x] = x
  rank[x] = 0

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



# Kruskal Algorithm with (Union-Find DS)

for pos_v in pos:
  make_set(pos_v)


edge_cnt = 0
mst_cost = 0

while edge_cnt < N - 1:
  cost, pos1, pos2 = edges.pop()

  if find(pos1) == find(pos2):
    continue

  union(pos1, pos2)
  edge_cnt += 1
  mst_cost += cost

print(mst_cost)
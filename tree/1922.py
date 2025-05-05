import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

edges: list[tuple[int, int, int]] = []

for i in range(M):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort(reverse=True)

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)

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

e_cnt = 0
cost = 0

while e_cnt < N - 1:
  c, a, b = edges.pop()

  if find(a) == find(b):
    continue

  union(a, b)

  e_cnt += 1
  cost += c

print(cost)
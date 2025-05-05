import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]

def union(x, y):
  rx, ry = find(x), find(y)
  
  if rank[rx] < rank[ry]:
    parent[rx] = ry
  else:
    parent[ry] = rx
    
    if rank[rx] == rank[ry]:
      rank[rx] += 1

for i in range(m):
  x, a, b = map(int, input().split())

  if x == 0:
    union(a, b)
  elif x == 1:
    if find(a) == find(b):
      print("YES")
    else:
      print("NO")


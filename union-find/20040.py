import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

parent = [i for i in range(n)]
rank = [0] * n

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

    if rank[ry] == rank[rx]:
      rank[rx] += 1 

  return

for i in range(1, m + 1):
  a, b = map(int, input().split())

  if find(a) == find(b):
    print(i)
    break
  
  union(a, b)
else:
  print(0)
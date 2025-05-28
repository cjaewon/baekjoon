import sys

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N):
  parent[i + 1] = int(input())

union_parent = [v for v in range(N + 1)]
rank = [0] * (N + 1)

def find(x):
  if union_parent[x] != x:
    union_parent[x] = find(union_parent[x])

  return union_parent[x]

def union(x, y):
  rx = find(x)
  ry = find(y)

  if rx == ry:
    return
  
  if rank[rx] > rank[ry]:
    union_parent[ry] = rx
  else:
    union_parent[rx] = ry

    if rank[rx] == rank[ry]:
      rank[ry] += 1

queries = [tuple(map(int, input().split())) for _ in range(N - 1 + Q)]
reversed_queries = list(reversed(queries))

for query in queries:
  if query[0] != 0:
    continue
  
  b = query[1]
  parent[b] = -parent[b]

visited = set()

def dfs(v):
  visited.add(v)

  if parent[v] <= 0:
    return

  if parent[v] not in visited:
    union(v, parent[v])
    dfs(parent[v])
  else:
    union(v, parent[v])

for v in range(1, N + 1):
  if v not in visited:
    dfs(v)

ans = []

for query in reversed_queries:
  match query:
    case (0, b):
      union(-parent[b], b)
    case (1, c, d):
      rc = find(c)
      rd = find(d)

      if rc == rd:
        ans.append("YES")
      else:
        ans.append("NO")

for a in reversed(ans):
  print(a)
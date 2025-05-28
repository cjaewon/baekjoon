import sys

sys.setrecursionlimit(10 ** 5)

input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
parent = [0 for i in range(N + 1)]
color = [0 for i in range(N + 1)]

for v in range(2, N + 1):
  parent[v] = int(input())

for i in range(1, N + 1):
  color[i] = int(input())

# union find with color union operation
u_parent = [v for v in range(N + 1)]
rank = [0 for i in range(N + 1)]
color_count = [set([color[i]]) for i in range(N + 1)]

def find(x):
  if u_parent[x] != x:
    u_parent[x] = find(u_parent[x])

  return u_parent[x]

def union(x, y):
  rx, ry = find(x), find(y)

  if rx == ry:
    return
  
  if rank[rx] > rank[ry]:
    u_parent[ry] = rx

    a, b = color_count[rx], color_count[ry]
    if len(a) < len(b):
      a, b = b, a
    
    for clr in b:
      a.add(clr)

    color_count[rx] = a
  else:
    u_parent[rx] = ry
    
    if rank[rx] == rank[ry]:
      rank[ry] += 1

    a, b = color_count[rx], color_count[ry]
    if len(a) < len(b):
      a, b = b, a
    
    for clr in b:
      a.add(clr)

    color_count[ry] = a

queries = [list(map(int, input().split())) for i in range(N + Q - 1)]
queries.reverse()

ans = []

for q in queries:
  match q:
    case [1, v]:
      union(v, parent[v])
    case [2, v]:
      rv = find(v)

      ans.append(len(color_count[rv]))

for s in reversed(ans):
  print(s)
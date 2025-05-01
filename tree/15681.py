import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10 ** 8)

N, R, Q = map(int, input().split())
tree = defaultdict(list)

for i in range(N - 1):
  u, v = map(int, input().split())

  tree[u].append(v)
  tree[v].append(u)

count = [0] * (N + 1)
visited = set()

def dfs(v):
  visited.add(v)

  s = 1

  for adj_v in tree[v]:
    if adj_v not in visited:
      s += dfs(adj_v)

  count[v] = s
  return s

dfs(R)

for i in range(Q):
  U = int(input())

  print(count[U])
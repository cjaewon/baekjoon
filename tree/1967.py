import sys

sys.setrecursionlimit(10 ** 9)

n = int(input())
graph = [[] for i in range(10001)]

for i in range(n - 1):
  a, b, c = map(int, sys.stdin.readline().split())

  graph[a].append((b, c))
  graph[b].append((a, c))

lengths = []
visted = [0 for i in range(10001)]

def dfs(v, l):
  visted[v] = True
  lengths.append((l, v))

  for b, c in graph[v]:
    if visted[b]:
      continue
    
    dfs(b, l + c)

dfs(1, 0)

max_len = max(lengths, key=lambda n: n[0])
lengths = []
visted = [0 for i in range(10001)]

dfs(max_len[1], 0)
print(max(lengths)[0])


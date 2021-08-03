import sys

sys.setrecursionlimit(10 ** 9)

n = int(input())
graph = [[] for i in range(100001)] # (v, w)

for i in range(n):
  info = list(map(int, sys.stdin.readline().split()))

  for i in range(1, len(info), 2):
    if info[i] == -1:
      break
    
    graph[info[0]].append((info[i], info[i + 1]))
    graph[info[i]].append((info[i], info[i + 1]))

visted = [0 for i in range(100001)]
lengths = [] # (len, v)

def dfs(v, len):
  lengths.append((len, v))
  visted[v] = 1  
  
  for nv, nw in graph[v]:
    if visted[nv]:
      continue

    dfs(nv, len + nw)

dfs(1, 0)

point1 = max(lengths, key=lambda n: n[0])
visted = [0 for i in range(100001)]
lengths = []

dfs(point1[1], 0)
print(max(lengths, key=lambda n: n[0])[0])
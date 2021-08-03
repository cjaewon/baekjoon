n = int(input())
parents = list(map(int, input().split()))
deleted_node = int(input())

graph = [[0 for i in range(n)] for i in range(n)]
visted = [[0 for i in range(n)] for i in range(n)]
root = 0
count = 0

for i, p in enumerate(parents):
  if p == -1:
    root = i
    continue

  graph[i][p] = 1
  graph[p][i] = 1

graph[deleted_node] = [0 for i in range(n)]

def dfs(v):
  global count

  leaf = True
  for i in range(0, len(graph[v])):
    if graph[v][i] != 1 or graph[i][v] != 1:
      continue

    leaf = False

    graph[v][i] = 0
    graph[i][v] = 0

    dfs(i)

  if leaf:
    count += 1

dfs(root)  

if deleted_node == root:
  count = 0

print(count)
from collections import deque

n, m, v = map(int, input().split())
graph = [[0 for j in range(n)] for i in range(n)]
visted = [0 for i in range(n)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a - 1][b - 1] = 1
  graph[b - 1][a - 1] = 1

def bfs(k):
  q = deque()

  visted[k] = 1
  q.append(k)

  while q:
    e = q.popleft()
    print(e + 1, end=" ")

    for i in range(n):
      if graph[e][i] == 1 and visted[i] == 0:
        visted[i] = 1
        q.append(i)
    
def dfs(k):
  visted[k] = 1
  print(k + 1, end=" ")

  for i in range(n):
    if graph[k][i] == 1 and visted[i] == 0:
      dfs(i)

dfs(v - 1)
print()
visted = [0 for j in range(n)]
bfs(v - 1) 

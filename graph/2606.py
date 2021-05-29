n = int(input())
edge = int(input())

graph = [[0 for j in range(n)] for i in range(n)]
visted = [0 for j in range(n)]
count = 0

def dfs(k):
  global count
  visted[k] = 1


  for i in range(n):
    if graph[k][i] == 1 and visted[i] == 0:
      count += 1
      dfs(i)
  


for i in range(edge):
  x, y = map(int, input().split())
  graph[x - 1][y - 1] = 1
  graph[y - 1][x - 1] = 1


dfs(0)
print(count)
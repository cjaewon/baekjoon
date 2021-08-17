from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for i in range(n)]
coins = [] # 첫 번째 코인 위치, 두 번째 코인 위치

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
  for j in range(m):
    if graph[i][j] == "o":
      coins.append((i, j))

coins.append(0)

def bfs():
  q = deque([coins])

  while q:
    coin1, coin2, count = q.popleft()

    if count > 10:
      return -1

    for i in range(4):
      prepared = []
  
      # coin1
      
      if not (0 <= coin1[0] + dy[i] <= n - 1 and 0 <= coin1[1] + dx[i] <= m - 1) and (0 <= coin2[0] + dy[i] <= n - 1 and 0 <= coin2[1] + dx[i] <= m - 1):
        return count + 1
      elif not (0 <= coin1[0] + dy[i] <= n - 1 and 0 <= coin1[1] + dx[i] <= m - 1):
        continue
      elif graph[coin1[0] + dy[i]][coin1[1] + dx[i]] == "#":
        prepared.append(coin1)
      else:
        prepared.append((coin1[0] + dy[i], coin1[1] + dx[i]))
      

      if not (0 <= coin2[0] + dy[i] <= n - 1 and 0 <= coin2[1] + dx[i] <= m - 1) and (0 <= coin1[0] + dy[i] <= n - 1 and 0 <= coin1[1] + dx[i] <= m - 1):
        return count + 1
      elif not (0 <= coin2[0] + dy[i] <= n - 1 and 0 <= coin2[1] + dx[i] <= m - 1):
        continue
      elif graph[coin2[0] + dy[i]][coin2[1] + dx[i]] == "#":
        prepared.append(coin2)
      else:
        prepared.append((coin2[0] + dy[i], coin2[1] + dx[i]))
      
      prepared.append(count + 1)
      q.append(prepared)

  return -1

d = bfs()

if d > 10:
  print("-1")
else:
  print(d)
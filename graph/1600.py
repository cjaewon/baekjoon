from collections import deque

K = int(input())
W, H = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(H)]
visited = [[[False for k in range(W)] for j in range(H)] for i in range(K + 1)]

queue = deque([(0, 0, K, 0)]) # y, x, K, distance

horse_delta = [(2, 1), (1, 2), (-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2)] # y, x
monkey_delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
  y, x, curr_K, dist = queue.popleft()

  if y == H - 1 and x == W - 1:
    print(dist)
    exit()

  if curr_K > 0:
    for dy, dx in horse_delta:
      if 0 <= y + dy < H and 0 <= x + dx < W:
        if not visited[curr_K - 1][y + dy][x + dx] and grid[y + dy][x + dx] != 1:
          visited[curr_K - 1][y + dy][x + dx] = True
          queue.append((y + dy, x + dx, curr_K - 1, dist + 1))
  
  for dy, dx in monkey_delta:
    if 0 <= y + dy < H and 0 <= x + dx < W:
      if not visited[curr_K][y + dy][x + dx] and grid[y + dy][x + dx] != 1:
        visited[curr_K][y + dy][x + dx] = True
        queue.append((y + dy, x + dx, curr_K, dist + 1))
    


print(-1)
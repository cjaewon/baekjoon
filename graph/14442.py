import sys
from collections import deque

N, M, K = map(int, input().split())
geo = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]

queue = deque([(0, 0, 0, K)]) # y, x, time, K
visited = [[[False for j in range(M)] for i in range(N)] for _ in range(K + 1)]

visited[K][0][0] = True

while queue:
  y, x, time, curr_K = queue.popleft()

  if y == N - 1 and x == M - 1:
    print(time + 1)
    exit()

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    new_y, new_x = y + dy, x + dx
    
    if 0 <= new_y < N and 0 <= new_x < M and not visited[curr_K - 1][new_y][new_x]:
      if geo[new_y][new_x] == 1 and curr_K > 0:
        visited[curr_K - 1][new_y][new_x] = True
        queue.append((new_y, new_x, time + 1, curr_K - 1))
      elif geo[new_y][new_x] == 0:
        visited[curr_K][new_y][new_x] = True
        queue.append((new_y, new_x, time + 1, curr_K))
    

print(-1)
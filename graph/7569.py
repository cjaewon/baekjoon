from collections import deque

M, N, H = map(int, input().split())
box = [[[] for j in range(N)] for i in range(H)]

start_point = []

for z in range(H):
  for y in range(N):
    box[z][y] = list(map(int, input().split()))

    for x, v in enumerate(box[z][y]):
      if v == 1:
        start_point.append((z, y, x, 0))

queue = deque(start_point)
last_time = 0

while queue:
  z, y, x, time = queue.popleft()
  delta = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)] # dz, dy, dx

  last_time = time

  for dz, dy, dx in delta:
    if 0 <= z + dz < H and 0 <= y + dy < N and 0 <= x + dx < M:
      if box[z + dz][y + dy][x + dx] == 0:
        box[z + dz][y + dy][x + dx] = 1
        queue.append((z + dz, y + dy, x + dx, time + 1))

for i in range(H):
  for j in range(N):
    for k in range(M):
      if box[i][j][k] == 0: # 시간이 지나도 다 안 익을 수 없는 경우
        print(-1)
        exit()

# 다 익었을 경우
print(last_time)

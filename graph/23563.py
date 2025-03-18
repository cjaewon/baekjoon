import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
table = [list(input()) for i in range(H)]

# 주위에 벽이 있는지 확인
def check(table, y, x) -> bool:
  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    new_y = y + dy
    new_x = x + dx

    if 0 <= new_y < H and 0 <= new_x < W:
      if table[new_y][new_x] == "#":
        return True
      
  return False


start_point, end_point = (0, 0), (0, 0)
checked_table = [[False for j in range(W)] for i in range(H)]

for i in range(H):
  for j in range(W):
    if table[i][j] == "S":
      start_point = (i, j)
    elif table[i][j] == "E":
      end_point = (i, j)
    
    checked_table[i][j] = check(table, i, j)

dq = deque([(*start_point, 0)])
min_time = [[float('inf') for j in range(501)] for i in range(501)]

min_time[start_point[0]][start_point[1]] = 0


while dq:
  y, x, time = dq.popleft()

  if table[y][x] == "E":
    print(time)
    break

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    new_y = y + dy
    new_x = x + dx

    if 0 <= new_y < H and 0 <= new_x < W:
      if table[new_y][new_x] == "#": continue
      
      if checked_table[y][x] and checked_table[new_y][new_x]:
        if time < min_time[new_y][new_x]:
          dq.appendleft((new_y, new_x, time))
          min_time[new_y][new_x] = time
      else:
        if time + 1 < min_time[new_y][new_x]:
          dq.append((new_y, new_x, time + 1))
          min_time[new_y][new_x] = time + 1



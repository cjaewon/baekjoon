import sys
from collections import deque

testcase = int(input())

for i in range(testcase):
  w, h = map(int, sys.stdin.readline().split())
  building = [list(sys.stdin.readline().rstrip()) for j in range(h)]

  start_point = deque([])

  for i in range(h):
    for j in range(w):
      if building[i][j] == "*":
        # fire
        start_point.appendleft((i, j, -1)) # y, x
      elif building[i][j] == "@":
        # player
        start_point.append((i, j, 0)) # y, x, time

  queue = deque(start_point)
  ans = -1
  while queue:
    y, x, time = queue.popleft()

    if time != -1 and not (0 < y < h - 1 and 0 < x < w - 1):
      ans = time
      break

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dy, dx in delta:
      if 0 <= y + dy < h and 0 <= x + dx < w:
        if building[y + dy][x + dx] != "." and building[y + dy][x + dx] != "@": continue

        if time == -1: # is fire
          building[y + dy][x + dx] = "*"
          queue.append((y + dy, x + dx, -1))
        else:
          building[y][x] = "*"

          queue.append((y + dy, x + dx, time + 1))
          building[y + dy][x + dx] = "*"
  if ans != -1:
    print(ans + 1)
  else:
    print("IMPOSSIBLE")


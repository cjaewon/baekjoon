import sys
from collections import deque

testcase = int(input())

for i in range(testcase):
  h, w = map(int, sys.stdin.readline().split())

  geo = [list(sys.stdin.readline().rstrip()) for i in range(h)]
  keys = [False for i in range(26)]

  for k in sys.stdin.readline().rstrip():
    if k == "0":
      continue

    keys[ord(k) - 97] = True

  new_key_find = True
  
  start_point = [] # 벽에 붙어있는 빈 공간

  for i in range(w):
    if geo[0][i] != "*":
      if geo[0][i].isupper() and keys[ord(geo[0][i]) - 65]:
        start_point.append((0, i))
      else:
        start_point.append((0, i))
    if geo[h - 1][i] != "*":
      if geo[h - 1][i].isupper() and keys[ord(geo[h - 1][i]) - 65]:
        start_point.append((h - 1, i))
      else:
        start_point.append((h - 1, i))

  for i in range(h):
    if geo[i][0] != "*":
      if geo[i][0].isupper() and keys[ord(geo[i][0]) - 65]:
        start_point.append((i, 0))
      else:
        start_point.append((i, 0))
    if geo[i][w - 1] != "*":
      if geo[i][w - 1].isupper() and keys[ord(geo[i][w - 1]) - 65]:
        start_point.append((i, w - 1))
      else:
        start_point.append((i, w - 1))

  stolen_document = 0

  # --- real logic ---

  while new_key_find:
    new_key_find = False
    visited = [[False for j in range(w)] for i in range(h)]

    queue = deque(start_point)

    while queue:
      y, x = queue.popleft()

      if geo[y][x] != ".":
        if geo[y][x] == "$":
          stolen_document += 1
          geo[y][x] = "."
        elif geo[y][x].islower():
          if not keys[ord(geo[y][x]) - 97]:
            new_key_find = True
            keys[ord(geo[y][x]) - 97] = True
            # geo[y][x] = "." 크게 의미 없는 코드인듯
        else: # geo[y][x].isupper():
          if not keys[ord(geo[y][x]) - 65]:
            continue

      for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= y + dy < h and 0 <= x + dx < w:
          if geo[y + dy][x + dx] != "*" and not visited[y + dy][x + dx]:
            visited[y + dy][x + dx] = True
            queue.append((y + dy, x + dx))
    
  print(stolen_document)
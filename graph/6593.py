from collections import deque

while True:
  L, R, C = map(int, input().split())

  if (L, R, C) == (0, 0, 0): break

  building = []

  for i in range(L):
    building.append([list(input()) for j in range(R)])
    input()

  for i in range(L):
    for j in range(R):
      for k in range(C):
        if building[i][j][k] == "S":
          start_point = (i, j, k)
        elif building[i][j][k] == "E":
          escape_point = (i, j, k)

  queue = deque([start_point + (0,)])
  delta = [(0, 1, 0), (0, 0, 1), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

  # visited = {}
  # visited[start_point] = True

  escaped = False

  while queue:
    z, y, x, time = queue.popleft()
    
    if (z, y, x) == escape_point:
      escaped = True
      break

    for dz, dy, dx in delta:
      if 0 <= z + dz < L and 0 <= y + dy < R and 0 <= x + dx < C:
        # if (z + dz, y + dy, x + dx) in visited: continue
        if building[z + dz][y + dy][x + dx] == "#": continue

        # visited[(z + dz, y + dy, x + dx)] = True
        building[z + dz][y + dy][x + dx] = "#"
        queue.append((z + dz, y + dy, x + dx, time + 1))

  if escaped:
    print(f"Escaped in {time} minute(s).")
  else:
    print("Trapped!")
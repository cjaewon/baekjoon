from collections import deque

table = [list(input().split()) for i in range(3)]
visited = {}

visited["".join([table[i][j] for i in range(3) for j in range(3)])] = True

queue = deque([])

for i in range(3):
  for j in range(3):
    if table[i][j] == "0":
      queue.append((i, j, 0, "".join([table[i][j] for i in range(3) for j in range(3)])))

if "".join([table[i][j] for i in range(3) for j in range(3)]) == "123456780":
  print(0)
  exit()

while queue:
  row, col, time, n_context = queue.popleft()

  for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

    if 0 <= row + dr < 3 and 0 <= col + dc < 3:
      context = list(n_context)

      i1 = (row+dr)*3 + (col+dc)
      i2 = context.index("0")

      context[i1], context[i2] = context[i2], context[i1]
      context_str = "".join(context)

      if context_str not in visited:
        if context_str == "123456780":
          print(time + 1)
          exit()

        visited[context_str] = True
        queue.append((row + dr, col + dc, time + 1, context_str))

print(-1)
from collections import deque

X = int(input())
path = [None for i in range(10 ** 6 + 1)]

if X == 1:
  print(0)
  print(1)
  exit()

q = deque([X])

while q:
  pos = q.popleft()

  if pos == 1:
    break

  if pos % 3 == 0 and path[pos // 3] == None:
    path[pos // 3] = pos
    q.append(pos // 3)
  if pos % 2 == 0 and path[pos // 2] == None:
    path[pos // 2] = pos
    q.append(pos // 2)
  if pos - 1 >= 0 and path[pos - 1] == None:
    path[pos - 1] = pos
    q.append(pos - 1)

cursor = 1
paths = []

while cursor is not None:
  paths.append(cursor)
  cursor = path[cursor]

print(len(paths) - 1)
print(" ".join(map(str, reversed(paths))))
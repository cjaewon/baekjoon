from collections import deque

X = int(input())

q = deque([(X, 0)])
visited = {X: True}

while q:
  pos, cost = q.popleft()

  if pos == 1:
    print(cost)
    break

  if pos % 3 == 0 and pos // 3 not in visited:
    visited[pos // 3] = True
    q.append((pos // 3, cost + 1))
  if pos % 2 == 0 and pos // 2 not in visited:
    visited[pos // 2] = True
    q.append((pos // 2, cost + 1))
  if pos - 1 >= 0 and pos - 1 not in visited:
    visited[pos - 1] = True
    q.append((pos - 1, cost + 1))

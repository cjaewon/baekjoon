from collections import deque

n = int(input())
table = [list(map(int, input())) for i in range(n)]

dq = deque([(0, 0, 0)]) # start y, start x, cost
min_cost = [[float('inf') for j in range(n)] for i in range(n)]

min_cost[0][0] = 0

while dq:
  y, x, cost = dq.popleft()

  if y == n - 1 and x == n - 1:
    print(cost)
    break

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    if 0 <= y + dy < n and 0 <= x + dx < n:
      if table[y + dy][x + dx] == 1:
        if cost < min_cost[y + dy][x + dx]:
          dq.appendleft((y + dy, x + dx, cost))
          min_cost[y + dy][x + dx] = cost
      else:
        if cost + 1 < min_cost[y + dy][x + dx]:
          dq.append((y + dy, x + dx, cost + 1))
          min_cost[y + dy][x + dx] = cost + 1

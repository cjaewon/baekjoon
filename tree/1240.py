from collections import deque

N, M = map(int, input().split())

tree = {}

for i in range(N - 1):
  a, b, cost = map(int, input().split())

  if a not in tree:
    tree[a] = [(b, cost)]
  else:
    tree[a].append((b, cost))

  if b not in tree:
    tree[b] = [(a, cost)]
  else:
    tree[b].append((a, cost))

for i in range(M):
  a, b = map(int, input().split())

  stack = deque([(a, 0)]) # pos, cost sum
  visited = {}

  while stack:
    pos, cost_sum = stack.pop()

    if pos == b:
      print(cost_sum)
      break


    for next_pos, cost in tree[pos]:
      if next_pos in visited: continue

      visited[next_pos] = True
      stack.append((next_pos, cost_sum + cost))

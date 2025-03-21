from collections import defaultdict, deque
import sys

N, K = map(int, input().split())

graph = defaultdict(list)

for i in range(K):
  A, B = map(int, sys.stdin.readline().split())

  if A == B: continue

  graph[A].append(B)
  graph[B].append(A)


for start_node in range(1, N + 1):
  queue = deque([(start_node, 0)])
  visited = [False for i in range(N + 1)]

  visited[0] = True
  visited[start_node] = True

  while queue:
    curr, cost = queue.popleft()

    if cost > 6:
      print("Big World!")
      exit()

    for neighbor in graph[curr]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append((neighbor, cost + 1))

  if list(filter(lambda visited: not visited, visited)):
    print("Big World!")
    exit()


print("Small World!")

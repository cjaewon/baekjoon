import sys
import heapq

graph = [[0 for j in range(1001)] for i in range(1001)]
n, m, x = map(int, input().split())

for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())

  if graph[a][b] != 0 and graph[a][b] < c:
    pass
  else:
    graph[a][b] = c

def dijkstra(start):
  distances = [float('inf') for i in range(1001)]
  distances[start] = 0
  q = []

  heapq.heappush(q, (distances[start], start))

  while q:
    distance, cursor = heapq.heappop(q)

    if distances[cursor] < distance:
      continue

    for i in range(len(graph[cursor])):
      if graph[cursor][i] != 0:
        if distances[i] > distance + graph[cursor][i]:
          distances[i] = distance + graph[cursor][i]
          heapq.heappush(q, (distances[i], i))
    
  return distances

round_distances = [0 for i in range(n + 1)]

for i in range(1, n + 1):
  distances = dijkstra(i)
  round_distances[i] = distances[x]

for i, distance in enumerate(dijkstra(x)):
  if i > n:
    break
  if i == 0:
    continue

  round_distances[i] += distance

print(max(round_distances)) 
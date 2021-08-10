import sys
import heapq

graph = [[-1 for j in range(1001)] for i in range(1001)]
n, e = map(int, input().split())

for i in range(e):
  a, b, c = map(int, sys.stdin.readline().split())
  
  if graph[a][b] != -1 and graph[a][b] < c:
    pass
  else:
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

def dijkstra(start):
  distances = [float('inf') for i in range(1001)]
  distances[start] = 0
  
  q = []
  heapq.heappush(q, (distances[start], start))

  while q:
    distance, cursor = heapq.heappop(q)

    if distance > distances[cursor]:
      continue

    for i in range(len(graph[cursor])):
      if graph[cursor][i] != -1:
        if distances[i] > distance + graph[cursor][i]:
          distances[i] = distance + graph[cursor][i]
          heapq.heappush(q, (distances[i], i))

  return distances

distances1 = dijkstra(1)
distances2 = dijkstra(v1)
distances3 = dijkstra(v2)

if min(distances1[v1] + distances2[v2] + distances3[n], distances1[v2] + distances2[n] + distances3[v1]) == float('inf'):
  print(-1)
else:
  print(min(distances1[v1] + distances2[v2] + distances3[n], distances1[v2] + distances2[n] + distances3[v1]))
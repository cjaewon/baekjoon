import sys
import heapq

n = int(input())
m = int(input())

graph = [[-1 for j in range(1001)] for i in range(1001)]

for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  
  if graph[a][b] != -1:
    graph[a][b] = c if graph[a][b] > c else graph[a][b]
  else:
    graph[a][b] = c
    
start, end = map(int, input().split())

def dijkstra(start):
  distances = [float('inf') for i in range(1001)]
  distances[start] = 0

  q = []
  heapq.heappush(q, (distances[start], start)) # 거리, 커서

  while q:
    distance, cursor = heapq.heappop(q)

    if distance > distances[cursor]:
      continue

    for i in range(len(graph[cursor])):
      if graph[cursor][i] != -1:
        if distance + graph[cursor][i] < distances[i]:
          distances[i] = distance + graph[cursor][i] 
          heapq.heappush(q, (distances[i], i))

  return distances

distances = dijkstra(start)
print(distances[end])
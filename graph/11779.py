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

def dijkstra(start, end):
  distances = [float('inf') for i in range(1001)]
  distances[start] = 0

  q = []
  result_road = []
  heapq.heappush(q, (distances[start], start, [start])) # 거리, 커서, 로드

  while q:
    distance, cursor, road = heapq.heappop(q)

    if distance > distances[cursor]:
      continue

    for i in range(len(graph[cursor])):
      if graph[cursor][i] != -1:
        if distance + graph[cursor][i] < distances[i]:
          distances[i] = distance + graph[cursor][i]
          if i == end:
            result_road = road + [i]
          heapq.heappush(q, (distances[i], i, road + [i]))

  return distances, result_road

distances, result_road = dijkstra(start, end)

print(distances[end])
print(len(result_road))
print(" ".join(map(str, result_road)))
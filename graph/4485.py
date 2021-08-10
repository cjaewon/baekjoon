import sys
import heapq

def dijkstra(graph, n):
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1] 
  
  distances = [[float('inf') for j in range(n)] for i in range(n)]
  distances[0][0] = graph[0][0]

  q = []
  heapq.heappush(q, (distances[0][0], (0, 0)))

  while q:
    distance, cursor = heapq.heappop(q)

    if distances[cursor[0]][cursor[1]] < distance:
      continue
    
    for i in range(4):
      if 0 <= cursor[0] + dy[i] <= n - 1 and 0 <= cursor[1] + dx[i] <= n - 1:
        if distances[cursor[0] + dy[i]][cursor[1] + dx[i]] > distance + graph[cursor[0] + dy[i]][cursor[1] + dx[i]]:
          distances[cursor[0] + dy[i]][cursor[1] + dx[i]] = distance + graph[cursor[0] + dy[i]][cursor[1] + dx[i]]
          heapq.heappush(q, (distances[cursor[0] + dy[i]][cursor[1] + dx[i]], (cursor[0] + dy[i], cursor[1] + dx[i])))
  
  return distances

i = 0
while True:
  n = int(input())

  if n == 0:
    break
  
  graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
  distances = dijkstra(graph, n)

  i += 1
  print("Problem {}: {}".format(i, distances[n - 1][n - 1]))
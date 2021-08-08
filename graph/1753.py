import sys
import heapq

graph = [[] for i in range(20001)]

v, e = map(int, input().split())
k = int(input())


for i in range(e):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))

def dijkstra(start):
  distances = {n: float('inf') for n in range(1, v + 1)}
  distances[start] = 0

  q = []
  heapq.heappush(q, [distances[start], start])

  while q:
    cost, curr = heapq.heappop(q)

    if cost > distances[curr]:
      continue 
      
    for i in range(len(graph[curr])):
      nextv = graph[curr][i][0]
      distance = cost + graph[curr][i][1]

      if distance < distances[nextv]:
        distances[nextv] = distance
        heapq.heappush(q, [distances[nextv], nextv])

  return distances

distances = dijkstra(k)

for i in range(1, v + 1):
  t = distances[i]

  if t == float('inf'):
    print("INF")
  else:
    print(t)

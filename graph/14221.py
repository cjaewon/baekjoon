import sys
import heapq

n, m = map(int, input().split())
graph = {}
# -1: 연결 x, 음수 제외한 정수: 가중치 

for i in range(m):
  a, b, c = map(int, sys.stdin.readline().split())

  if a not in graph:
    graph[a] = [(b, c)]
  else:
    graph[a].append((b, c))

  if b not in graph:
    graph[b] = [(a, c)]
  else:
    graph[b].append((a, c))

p, q = map(int, input().split())

homes = list(map(int, input().split()))
convenience_stores = list(map(int, input().split()))

def dijkstra(pq):
  # pq = [(0, start_point)]

  dist = [float('inf') for i in range(5001)]

  for _, node in pq:
    dist[node] = 0

  while pq:
    curr_dist, cursor = heapq.heappop(pq)

    if dist[cursor] < curr_dist:
      continue

    for next_point, w in graph[cursor]:
      if curr_dist + w < dist[next_point]:
        heapq.heappush(pq, (curr_dist + w, next_point))
        dist[next_point] = curr_dist + w

  return dist

dist = dijkstra([(0, node) for node in convenience_stores])

min_dist = float('inf')
idx = -1

for i in range(n + 1):
  if i in homes and dist[i] < min_dist:
    min_dist = dist[i]
    idx = i

print(idx)
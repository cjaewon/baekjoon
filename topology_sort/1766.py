import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]
indeg = [0 for i in range(N + 1)]

for i in range(M):
  A, B = map(int, input().split())
  # A -> B

  graph[A].append(B)
  indeg[B] += 1

pq = [i for i in range(1, N + 1) if indeg[i] == 0]
heapq.heapify(pq)

while pq:
  v = heapq.heappop(pq)

  print(v, end=" ")

  for adj_v in graph[v]:
    indeg[adj_v] -= 1

    if indeg[adj_v] == 0:
      heapq.heappush(pq, adj_v)
import heapq

m, n = map(int, input().split())
graph = [list(map(int, list(input()))) for i in range(n)]

def dijkstra():
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  distances = [[float('inf') for j in range(m)] for i in range(n)]
  distances[0][0] = 0

  q = []
  heapq.heappush(q, (distances[0][0], (0, 0)))

  while q:
    distance, cursor = heapq.heappop(q)

    if distances[cursor[0]][cursor[1]] < distance:
      continue

    for i in range(4):
      if 0 <= cursor[0] + dy[i] <= n - 1 and 0 <= cursor[1] + dx[i] <= m - 1:
        if distances[cursor[0] + dy[i]][cursor[1] + dx[i]] > distance + graph[cursor[0] + dy[i]][cursor[1] + dx[i]]:
          distances[cursor[0] + dy[i]][cursor[1] + dx[i]] = distance + graph[cursor[0] + dy[i]][cursor[1] + dx[i]]
          heapq.heappush(q, (distances[cursor[0] + dy[i]][cursor[1] + dx[i]], (cursor[0] + dy[i], cursor[1] + dx[i])))
  
  return distances

distances = dijkstra()
print(distances[n - 1][m - 1])
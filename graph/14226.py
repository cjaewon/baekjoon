from collections import deque

s = int(input())
visited = [[0 for i in range(1001)] for i in range(1001)]

def bfs():
  q = deque()
  q.append((1, 0, 0)) # (screen, clipboard, time)

  while q:
    screen, clipboard, time = q.popleft()

    if screen > 1000 or clipboard > 1000:
      continue

    if visited[screen][clipboard]:
      continue

    if screen == s:
      print(time)
      return

    visited[screen][clipboard] = 1

    q.append((screen, screen, time + 1))
    q.append((screen + clipboard, clipboard, time + 1))
    
    if screen > 0:
      q.append((screen - 1, clipboard, time + 1))

bfs()
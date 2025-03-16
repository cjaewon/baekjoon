from collections import deque

N, K = map(int, input().split()) # N: 수빈의 처음 위치, K: 동생의 처음 위치
q = deque([(K,  0)]) # 역추척으로 가자. (동생의 위치, 걸린 시간)

visited = [False for i in range(100001)]
visited[K] = True

path = [None for i in range(100001)]

while q:
  pos, time = q.popleft()

  if pos == N:
    print(time)
    
    cursor = pos

    while cursor is not None:
      print(cursor, end=" ")
      
      cursor = path[cursor]

    break

  if pos % 2 == 0:
    check = [pos - 1, pos + 1, pos // 2]
  else:
    check = [pos - 1, pos + 1]

  for next_pos in check:
    if 0 <= next_pos <= 100000 and not visited[next_pos]:
      path[next_pos] = pos
      visited[next_pos] = True
      q.append((next_pos, time + 1))


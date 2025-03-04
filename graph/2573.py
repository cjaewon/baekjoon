from collections import deque

N, M = map(int, input().split()) # N: 행의 개수, M: 열의 개수

area = [list(map(int, input().split())) for i in range(N)]

def melt():
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  for i in range(N):
    for j in range(M):
      if area[i][j] == 0:
        continue

      water = 0
      
      for k in range(4):
        if 0 <= i + dy[k] < N and 0 <= j + dx[k] < M:
          if area[i + dy[k]][j + dx[k]] == 0:
            water += 1
      
      area[i][j] -= water

      if area[i][j] == 0:
        area[i][j] = -1

      # if area[i][j] < 0:
        # area[i][j] = 0
  for i in range(N):
    for j in range(M):
      if area[i][j] < 0:
        area[i][j] = 0


def check():
  point = None
  visited = [[False for j in range(M)] for i in range(N)]

  for i in range(N):
    for j in range(M):
      if area[i][j] != 0:
        point = (i, j)
        break
    if point:
      break
  
  if point is None:
    return 0  # 분리 ㄴㄴ -> 다 녹음
  
  q = deque([point])
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  visited[point[0]][point[1]] = True

  while q:
    cursor = q.popleft()

    for k in range(4):
      if 0 <= cursor[0] + dy[k] < N and 0 <= cursor[1] + dx[k] < M:
        if area[cursor[0] + dy[k]][cursor[1] + dx[k]] != 0 and not visited[cursor[0] + dy[k]][cursor[1] + dx[k]]:
          visited[cursor[0] + dy[k]][cursor[1] + dx[k]] = True
          q.append((cursor[0] + dy[k], cursor[1] + dx[k]))

  for i in range(N):
    for j in range(M):
      if area[i][j] != 0 and not visited[i][j]:
        return 1 # 분리 ㅇㅇ

  return 2 # 분리 ㄴㄴ


year = 0

while True:
  checked = check()
  
  if checked == 0:
    print(0)
    break
  elif checked == 1:
    print(year)
    break
  else: # checked == 2
    melt()

  year += 1
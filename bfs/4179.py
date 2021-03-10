# EOF 에러 뜸 왜 이러는지는 모르겠음

from collections import deque

# 행이 y 열이 x
r, c = map(int, input().split(' '))
table = [list(input()) for i in range(r)]
# TIL: 파이썬에서 "123".split(""), () 말고 list("123") 으로 해야 ["1", "2", "3"] 이 나온다. 

# table에 지나간 자리를 벽으로 변경하지 않고 check를 사용해서 지나간 자리를 표시한다. 그 이유는 불이랑 같이 사용하기 때문이다.
# 1은 지훈이가 지나간 자리, 2는 불이 지나간 자리 (2이면 지훈이가 지나 갈 수 없다.)
# check가 1인 자리에는 지훈이가 지나갈 필요가 없다. 이미 지나갔기 떄문에 하지만 불은 지나갈 수 있다.
# check = 2 가 되면 마찬가지로 지훈이는 지나 갈 수 없고 불이 지나갔다는 것 또한 알려줄 수 있음
check = [[0 for i in range(c)] for j in range(r)] 

q = deque()
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for i in range(r):
  for j in range(c):
    if table[i][j] == "J":
      # y, x, 지훈 = 0, 불 = 1, 걸린 시간 (지훈이만)
      q.append((i, j, 0, 1))
      check[i][j] = 1
    elif table[i][j] == "F":
      q.appendleft((i, j, 1)) 
      check[i][j] = 2

while True:
  e = q.popleft()

  for i in range(4):
    y = e[0] + dy[i]
    x = e[1] + dx[i]

    if y <= r - 1 and y >= 0 and x <= c - 1 and x >= 0:
      if e[2] == 0 and check[y][x] == 0 and table[y][x] == ".": # 지훈이
        check[y][x] = 1
        q.append((y, x, 0, e[3] + 1)) 
      elif (check[y][x] == 0 or check[y][x] == 1) and (table[y][x] == "." or table[y][x] == "J"): # 불
        check[y][x] = 2
        q.append((y, x, 1))
  
  if e[2] == 0 and (e[0] == 0 or e[0] == r - 1 or e[1] == c - 1 or e[1] == 0):
    print(e[3])
    break

  if not q:
    print("IMPOSSIBLE")
    break


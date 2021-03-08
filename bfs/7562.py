# TIL: queue.Queue 는 멀티스레드를 위한 큐라서 느리기 때문에 단순 자료구조로써 queue는 collections의 deque를 써야한다. 
# https://www.acmicpc.net/board/view/38423#comment-70882

from collections import deque

def solve():
  q = deque()

  l = int(input())

  check = [[0 for i in range(l)] for i in range(l)]

  x, y = map(int, input().split(' '))
  xx, yy = map(int, input().split(' '))

  dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

  q.append((y, x, 0))
  check[y][x] = 1

  while q:
    e = q.popleft()

    if e[0] == yy and e[1] == xx:
      print(e[2])
      return

    for i in range(len(dx)):
      if e[1] + dx[i] <= l - 1 and e[1] + dx[i] >= 0 and e[0] + dy[i] <= l - 1 and e[0] + dy[i] >= 0 and check[e[0] + dy[i]][e[1] + dx[i]] == 0:
        check[e[0] + dy[i]][e[1] + dx[i]] = 1
        q.append((e[0] + dy[i], e[1] + dx[i], e[2] + 1))

if __name__ == "__main__":
  n = int(input())

  for i in range(n):
    solve()
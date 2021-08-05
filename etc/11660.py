# x, y 행과 열을 헷갈렸던 문제

import sys

n, m = map(int, input().split())
table = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
presum = [[0 for j in range(n + 1)] for i in range(n)]

for i in range(n):
  for j in range(n):
    presum[i][j + 1] = presum[i][j] + table[i][j]

for i in range(m):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

  s = 0

  for x in range(x1 - 1, x2):
    s += presum[x][y2] - presum[x][y1 - 1]
  print(s)
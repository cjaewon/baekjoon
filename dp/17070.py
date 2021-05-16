from collections import deque
import sys
import pprint

n = int(input())
table = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dp = [[[0 for k in range(3)] for j in range(n)] for i in range(n)]

# table[0][0] = table[0][1] = 1
q = deque()
count = 0

# 0 가로, 1 세로, 2 대각선
dp[0][1][0] = 1

def check(row: int, col: int) -> bool:
  if row < n and col < n and table[row][col] == 0:
    return True

  return False

for i in range(n):
  for j in range(n):
    if table[i][j] == 1:
      continue
    if check(i, j + 1):
      dp[i][j + 1][0] += dp[i][j][0]
    if check(i + 1, j + 1) and check(i, j + 1) and check(i + 1, j):
      dp[i + 1][j + 1][2] += dp[i][j][0]
    if check(i + 1, j):
      q.append((i + 1, j, 1))
      dp[i + 1][j][1] += dp[i][j][1]
    if check(i + 1, j + 1) and check(i, j + 1) and check(i + 1, j):
      dp[i + 1][j + 1][2] += dp[i][j][1]
    if check(i, j + 1):
      dp[i][j + 1][0] += dp[i][j][2]
    if check(i + 1, j):
      dp[i + 1][j][1] += dp[i][j][2]
    if check(i + 1, j + 1) and check(i, j + 1) and check(i + 1, j):
      dp[i + 1][j + 1][2] += dp[i][j][2]

print(sum(dp[n - 1][n - 1]))
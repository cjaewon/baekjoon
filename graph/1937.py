import sys
from functools import cache

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
memo = {}

def dfs(y, x):
  if (y, x) in memo:
    return memo[(y, x)]
  
  candidates = []

  for dy, dx in [(0, 1), (1, 0), (0, -1), (-1 ,0)]:
    if 0 <= y + dy < n and 0 <= x + dx < n and grid[y + dy][x + dx] > grid[y][x]:
      candidates.append(dfs(y + dy, x + dx) + 1)

  if not candidates:
    memo[(y, x)] = 1
  else:
    memo[(y, x)] = max(candidates)

  return memo[(y, x)]

for y in range(n):
  for x in range(n):
    dfs(y, x)

print(max(memo.values()))
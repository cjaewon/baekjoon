import sys
from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for i in range(r)]

alphabet = [0 for i in range(26)]
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
maxlen = 0

def dfs(x, y, len):
  global maxlen

  if maxlen < len:
    maxlen = len

  alphabet[ord(graph[x][y]) - 65] = 1


  for i in range(4):
    if 0 <= x + dx[i] <= r - 1 and 0 <= y + dy[i] <= c - 1:
      char = graph[x + dx[i]][y + dy[i]]

      if alphabet[ord(char) - 65]:
        continue

      dfs(x + dx[i], y + dy[i], len + 1)  

  alphabet[ord(graph[x][y]) - 65] = 0

dfs(0, 0, 1)
print(maxlen)


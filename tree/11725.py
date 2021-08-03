"""
처음에는 그냥 dfs로 하나하나 다 찾아볼려고 했는데 시간초과가 나왔다.
그래서 풀이를 보고 dfs 한번에 answer 배열에 넣는 방식으로 변경하였다.
"""

import sys

sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
graph = [[] for i in range(100001)]
visted = [0 for i in range(100001)]
answer = [0 for i in range(100001)]

for i in range(n - 1):
  a, b = map(int, sys.stdin.readline().split(" "))

  graph[a].append(b)
  graph[b].append(a)

def dfs(i):
  visted[i] = 1

  for k in graph[i]:
    if visted[k]:
      continue

    
    answer[k] = i
    dfs(k)

dfs(1)

for i in range(2, n + 1):
  print(answer[i])


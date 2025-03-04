import sys
from collections import deque


def run():
  N = int(input())
  tree = [0 for i in range(N + 1)]

  for i in range(N - 1):
    A, B = map(int, sys.stdin.readline().rstrip().split()) # A가 B의 부모

    tree[B] = A

  a, b = map(int, input().split())
  
  visited = [False for i in range(N + 1)]
  q = deque([a, b])

  while q:
    elem = q.popleft()

    if elem == 0:
      continue

    if visited[elem]:
      print(elem)
      return
    
    visited[elem] = True

    q.append(tree[elem])




T = int(input()) # T: 테스트 케이스

for i in range(T):
  run()
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

parent = {}
size = {}

def find(x):
  if x not in parent:
    parent[x] = x
    size[x] = 1

  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]

def union(x, y):
  rx, ry = find(x), find(y)
  
  if rx == ry:
    return
  
  if size[rx] > size[ry]:
    parent[ry] = rx
    size[rx] += size[ry]
  else:
    parent[rx] = ry
    size[ry] += size[rx]

for _ in range(T):
  F = int(input())

  parent = {}
  size = {}

  for _ in range(F):
    x, y = input().split()
    union(x, y)

    rx = find(x)
    print(size[rx])


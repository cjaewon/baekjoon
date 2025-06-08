import sys
import heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())

is_not_tree = [False for i in range(N + 1)]
parent = [i for i in range(N + 1)]
size = [1 for i in range(N + 1)]
min_v = [i for i in range(N + 1)]

def find(x: int):
  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]

def union(x: int, y: int):
  rx, ry = find(x), find(y)

  if rx == ry:
    return
  
  if size[rx] > size[ry]:
    parent[ry] = rx
    size[rx] += size[ry]
    min_v[rx] = min(min_v[rx], min_v[ry])
  else:
    parent[rx] = ry
    size[ry] += size[rx]
    min_v[ry] = min(min_v[rx], min_v[ry])

pq = [(-size[i], i) for i in range(1, N + 1)]
lazy_del: dict[tuple[int, int], int] = defaultdict(int)

heapq.heapify(pq)

for _ in range(Q):
  cmd = list(map(int, input().split()))

  match cmd:
    case [1, u, v]:
      ru, rv = find(u), find(v)

      if ru == rv:
        is_not_tree[ru] =  True
        lazy_del[(-size[ru], min_v[ru])] += 1
      elif is_not_tree[ru] or is_not_tree[rv]:
        if not is_not_tree[ru]:
          lazy_del[(-size[ru], min_v[ru])] += 1
        if not is_not_tree[rv]:
          lazy_del[(-size[rv], min_v[rv])] += 1

        union(u, v)
        new_ru = find(u)

        is_not_tree[new_ru] = True
      else:
        lazy_del[(-size[ru], min_v[ru])] += 1
        lazy_del[(-size[rv], min_v[rv])] += 1

        union(u, v)
        new_ru = find(u)

        heapq.heappush(pq, (-size[new_ru], min_v[new_ru]))
    case [2]:
      while pq:
        x = heapq.heappop(pq)

        if lazy_del[x] > 0:
          lazy_del[x] -= 1
        else:
          # if not is_not_tree[find(x[1])]:
          #   break
          break
        
      print(x[1])
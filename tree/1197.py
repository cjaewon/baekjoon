# 스패닝 트리 (Spanning Tree) : Graph의 모든 정점을 포함하는 트리 형태의 부분 그래프
#   - 존재 조건: Graph가 연결 그래프여야함.
# 트리 :
#   - 무방향이면서 사이클이 없는 연결 그래프
#   - V개의 정점, V-1개의 간선을 가지는 연결 그래프
#   - 임의의 두 점을 연결하는 simple path가 유일한 그래프
# 최소 스패닝 트리 (MST) : 스패닝 트리 중에 간선의 가중치의 합이 가장 적은 스패닝 트리

# Kruskal Algorithm with (Union-Find DS)

import sys

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 8)

V, E = map(int, input().split())

edges = []

for i in range(E):
  A, B, C = map(int, input().split())
  edges.append((C, A, B))

edges.sort(reverse=True)


parent = [i for i in range(V + 1)]
rank = [0] * (V + 1)

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])

  return parent[x]

def union(x, y):
  rx, ry = find(x), find(y)

  if rx == ry:
    return

  if rank[rx] > rank[ry]:
    parent[ry] = rx
  else:
    parent[rx] = ry

    if rank[rx] == rank[ry]:
      rank[ry] += 1

curr_v = 0
edge_w_sum = 0

while curr_v < V - 1:
  C, A, B = edges.pop()

  if find(A) == find(B):
    continue
  else:
    curr_v += 1
    edge_w_sum += C

    union(A, B)

print(edge_w_sum)

# Kruskal Algorithm with dfs(only-A-B-check)

# import sys
# import heapq
# from collections import defaultdict

# input = lambda: sys.stdin.readline().rstrip()

# sys.setrecursionlimit(10 ** 8)

# V, E = map(int, input().split())
# minheap = []

# for i in range(E):
#   A, B, C = map(int, input().split())

#   heapq.heappush(minheap, (C, A, B))

# graph = defaultdict(set)

# def connect_check_dfs(v: int, target: int, visited: set):
#   if v == target:
#     return True
  
#   visited.add(v)

#   for adj_v in graph[v]:
#     if adj_v not in visited:
#       if connect_check_dfs(adj_v, target, visited):
#         return True

#   return False
  

# mst_w_sum = 0
# v_cnt = 0

# while minheap and v_cnt <= V - 1:
#   C, A, B = heapq.heappop(minheap)

#   if B in graph[A]:
#     continue

#   visited = set()

#   if connect_check_dfs(A, B, visited):
#     continue

#   graph[A].add(B)
#   graph[B].add(A)

#   mst_w_sum += C
#   v_cnt += 1

# print(mst_w_sum)


# Kruskal Algorithm with dfs(all-check)

# import sys
# import heapq
# from collections import defaultdict

# input = lambda: sys.stdin.readline().rstrip()

# sys.setrecursionlimit(10 ** 8)

# V, E = map(int, input().split())
# minheap = []

# for i in range(E):
#   A, B, C = map(int, input().split())

#   heapq.heappush(minheap, (C, A, B))

# graph = defaultdict(set)

# def cycle_check_dfs(v: int, parent: int, visited: set):
#   visited.add(v)

#   for adj_v in graph[v]:
#     if adj_v == parent:
#       continue

#     if adj_v in visited:
#       return True
    
#     if cycle_check_dfs(adj_v, v, visited):
#       return True
    
#   return False

# mst_w_sum = 0
# v_cnt = 0

# while minheap and v_cnt <= V - 1:
#   C, A, B = heapq.heappop(minheap)

#   if B in graph[A]:
#     continue

#   graph[A].add(B)
#   graph[B].add(A)

#   mst_w_sum += C
#   v_cnt += 1
#   visited = set()

#   for v in range(1, V + 1):
#     if v in visited:
#       continue

#     is_cycle = cycle_check_dfs(v, None, visited)

#     if is_cycle:
#       graph[A].discard(B)
#       graph[B].discard(A)
#       mst_w_sum -= C
#       v_cnt -= 1
      
#       break

# print(mst_w_sum)

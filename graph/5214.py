"""
하이퍼튜브라는 새로운 정점을 만드는게 어떨까

바로 그래프 끼리 연결한다면
그래프를 만드는데 O(MK^2)의 시간복잡도를 지니는데
하이퍼튜브 정점을 만든다면 단순히 O(MK)로 처리할 수 있음.

그럼 하이퍼튜브 정점을 만드는게 최적해, 즉 정답을 보장해주는가에 대해 고민해봐야함.
"""

import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

N, K, M = map(int, input().split())

graph: dict[int, list] = defaultdict(list)

for hypertube in range(M):
  for station in map(int, input().split()):
    graph[-hypertube].append(station)
    graph[station].append(-hypertube)

start = 1
end = N

q = deque([(start, 1)]) 
visited = set([start])

while q:
  v, cnt = q.popleft()

  if v == end:
    print(cnt)
    break

  for adj_v in graph[v]:
    if adj_v not in visited:
      visited.add(adj_v)
      q.append((adj_v, cnt + (0 if adj_v <= 0 else 1)))
else:
  print(-1)
"""
Treap을 이용한 시도 -> 시간 초과로 탈락
이론상 O(nlogn) 이므로 통과되어야 하지만 상수 시간이 커서 통과되지 않는 것 같음.

lazy deletion + heapq를 활용하자.

heapq에는 (value, index)를 넣고 index를 넘어가면 그냥 버리는걸로 하자.
이것도 시간 복잡도는 O(nlogn)에 근사

-> lazy out of bounds deletion?
"""

import heapq

N, L = map(int, input().split())
nums = [0] + list(map(int, input().split()))

minheap = []

for i in range(1, len(nums)):
  heapq.heappush(minheap, (nums[i], i))

  while minheap[0][1] < i - L + 1:
    heapq.heappop(minheap)

  print(minheap[0][0], end=" ")
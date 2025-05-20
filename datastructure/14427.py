"""
nums = [...]

1 i v : index i를 v로 바꾼다.
  - 이건 그냥 숫자 바꾸기로 이해할 수 있을 것 같다.
  - nums[i] -> v로 

  - lazy deletion을 이용해서 nums[i]를 삭제했다 치고 그냥 v를 minheap 추가로 넣자.
2 : min 출력

인덱스는 1부터 시작
index 관련해서 물어봄으로 index도 minheap, lazy_del dict에 같이 주자.
"""

import sys
import heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [0] + list(map(int, input().split()))

minheap = [(nums[i], i) for i in range(1, N + 1)]
heapq.heapify(minheap)

M = int(input())
lazy_del = defaultdict(int)

for _ in range(M):
  cmd = list(map(int, input().split()))

  match cmd:
    case [1, i, v]:
      lazy_del[(nums[i], i)] += 1
      nums[i] = v
      
      heapq.heappush(minheap, (v, i))
    case [2]:
      while minheap:
        x = minheap[0]

        if lazy_del[x] <= 0:
          break
        else:
          heapq.heappop(minheap)
          lazy_del[x] -= 1

      print(minheap[0][1])
      
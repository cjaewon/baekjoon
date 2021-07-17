"""
최소 힙 관련 문제
11279번 최대 힙 문제를 풀때는 최소 힙과 마찬가지로 0으로 초기화 하여, curr * 2 + 1 > end 일때에도 heap[curr * 2] >= heap[curr * 2 + 1] 조건문에서 
계속 성립해서 상관 없었는데 최소 힙 관련 문제에서는 heap[curr * 2 + 1] 이 0 될 경우에 오류가 발생해서 
curr * 2 + 1 <= end과 포함 된 조건문을 하나 더 추가해서 해결했다.
"""

import sys

n = int(input())
heap = [0 for i in range(100001)]
end = 0

for i in range(n):
  x = int(sys.stdin.readline())
  # print("start", end, heap[0:20])
  if x == 0:
    if end == 0:
      print(heap[1])
      continue

    print(heap[1])
    heap[1] = heap[end]
    heap[end] = 0
    end -= 1

    curr = 1
    while curr <= end:
      if curr * 2 <= end and heap[curr * 2] < heap[curr] and heap[curr * 2] <= heap[curr * 2 + 1]:
        heap[curr * 2], heap[curr] = heap[curr], heap[curr * 2]
        curr = curr * 2
      elif curr * 2 <= end and heap[curr * 2] < heap[curr] and curr * 2 + 1 > end:
        heap[curr * 2], heap[curr] = heap[curr], heap[curr * 2]
        curr = curr * 2
      elif curr * 2 + 1 <= end and heap[curr * 2 + 1] < heap[curr] and heap[curr * 2 + 1] <= heap[curr * 2]:
        heap[curr * 2 + 1], heap[curr] = heap[curr], heap[curr * 2 + 1]
        curr = curr * 2 + 1
      else:
        break
  else:
    end += 1
    heap[end] = x

    curr = end

    while curr // 2 >= 1:
      if heap[curr // 2] > heap[curr]:
        heap[curr // 2], heap[curr] = heap[curr], heap[curr // 2]

      curr = curr // 2
  # print("end", end, heap[0:20])
  
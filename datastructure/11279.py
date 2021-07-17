"""
최대힙 관련 문제
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
      if curr * 2 <= end and heap[curr * 2] > heap[curr] and heap[curr * 2] >= heap[curr * 2 + 1]:
        heap[curr * 2], heap[curr] = heap[curr], heap[curr * 2]
        curr = curr * 2
      elif curr * 2 + 1 <= end and heap[curr * 2 + 1] > heap[curr] and heap[curr * 2 + 1] >= heap[curr * 2]:
        heap[curr * 2 + 1], heap[curr] = heap[curr], heap[curr * 2 + 1]
        curr = curr * 2 + 1
      else:
        break
  else:
    end += 1
    heap[end] = x

    curr = end

    while curr // 2 >= 1:
      if heap[curr // 2] < heap[curr]:
        heap[curr // 2], heap[curr] = heap[curr], heap[curr // 2]
      curr = curr // 2
  # print("end", end, heap[0:20])
  
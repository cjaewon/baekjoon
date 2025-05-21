import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

card_sets = [int(input()) for i in range(N)]
minheap = card_sets.copy()

heapq.heapify(minheap)
cnt = 0

while len(minheap) > 1:
  x = heapq.heappop(minheap)
  y = heapq.heappop(minheap)

  heapq.heappush(minheap, x + y)
  cnt += x + y

print(cnt)
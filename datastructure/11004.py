import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
As = list(map(int, input().split()))

maxheap = []

for A in As:
  if len(maxheap) < K:
    heapq.heappush(maxheap, -A)
  else:
    if A < -maxheap[0]:
      heapq.heappushpop(maxheap, -A)

print(-sorted(maxheap, reverse=True)[K - 1])

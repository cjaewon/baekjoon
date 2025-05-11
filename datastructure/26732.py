import sys
import heapq

input = lambda: sys.stdin.readline()

N = int(input())
As = sorted(list(map(int, input().split())))

maxheap = []

weight = 2
time = 0

is_nie = False

for i in range(len(As)):
  if weight >= As[-1]:
    break

  if weight <= As[i]:
    while maxheap:
      last = -heapq.heappop(maxheap)
      weight += last
      time += 1

      if weight > As[i] or weight >= As[-1]:
        break
    else:
      if weight < As[-1]:
        is_nie = True
        break

  heapq.heappush(maxheap, -As[i])


if is_nie:
  print("NIE")
else:
  print(time)
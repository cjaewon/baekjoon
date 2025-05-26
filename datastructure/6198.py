import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

building_heights = [int(input()) for i in range(N)]
mstack = []

ans = 0

for i in range(N - 1, -1, -1):
  h = building_heights[i]

  while mstack:
    if h > building_heights[mstack[-1]]:
      mstack.pop()
    else:
      break
  
  if mstack:
    ans += (mstack[-1] - i - 1)
  else:
    ans += N - 1 - i + 1 - 1
  mstack.append(i)

print(ans)

# N - 1 - i - 2
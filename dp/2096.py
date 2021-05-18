import sys

n = int(input())
a, b, c = map(int, sys.stdin.readline().split())

maxdp = [a, b, c]
mindp = [a, b, c]
maxtemp = [0, 0, 0]
mintemp = [0, 0, 0]

for i in range(n - 1):
  a, b, c = map(int, sys.stdin.readline().split())

  maxtemp[0] = max(maxdp[0], maxdp[1]) + a
  maxtemp[1] = max(maxdp[0], maxdp[1], maxdp[2]) + b
  maxtemp[2] = max(maxdp[1], maxdp[2]) + c

  maxdp[0] = maxtemp[0]
  maxdp[1] = maxtemp[1]
  maxdp[2] = maxtemp[2]

  mintemp[0] = min(mindp[0], mindp[1]) + a
  mintemp[1] = min(mindp[0], mindp[1], mindp[2]) + b
  mintemp[2] = min(mindp[1], mindp[2]) + c

  mindp[0] = mintemp[0]
  mindp[1] = mintemp[1]
  mindp[2] = mintemp[2]

print(max(maxdp), min(mindp))
import sys

n, m = map(int, input().split())
data = [0]
s = 0

for i in list(map(int, input().split())):
  s += i
  data.append(s)

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())

  print(data[b] - data[a - 1])
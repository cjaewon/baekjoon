import sys
import math
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lines = []

for _ in range(N):
  a, b, c = map(int, input().split())

  if a == 0:
    lines.append((0, 1))
    continue
  if b == 0:
    lines.append((1, 0))
    continue

  if a < 0:
    a = -a
    b = -b

  lines.append((a // math.gcd(a, b), b // math.gcd(a, b)))

lines_setcount = Counter(lines)

cnt = 0

for i in range(N):
  cnt += N - lines_setcount[lines[i]]

print(cnt // 2)
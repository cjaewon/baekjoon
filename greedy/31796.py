import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = list(map(int, input().split()))

S.sort()

i = len(S) - 1
standard = S[i]
page = 1

while i >= 0:
  if standard / 2 >= S[i]:
    standard = S[i]
    page += 1

  i -= 1
print(page)
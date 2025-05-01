N = int(input())
X, S = map(int, input().split())

for i in range(N):
  c, p = map(int, input().split())

  if X < c or p <= S:
    continue

  print("YES")
  break
else:
  print("NO")
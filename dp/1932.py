n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
dp = [[0 for j in range(i)] for i in range(1, n + 1)]

for i in range(n):
  k = n - i - 1

  if k == 0:
    break

  for j in range(len(data[k]) - 1):
    dp[k - 1][j] = max(dp[k][j] + data[k][j], dp[k][j + 1] + data[k][j + 1])

print(dp[0][0] + data[0][0])
n, k = map(int, input().split())

w = [0 for i in range(n + 1)]
v = [0 for i in range(n + 1)]

dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
# dp[i][k] i번째까지 물건을 담을 수 있는 크기가 최대 k일때 최대의 만족도 

for i in range(1, n + 1):
  w[i], v[i] = map(int, input().split())

for i in range(1, n + 1):
  for j in range(1, k + 1):
    if j - w[i] < 0:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])

print(dp[n][k])
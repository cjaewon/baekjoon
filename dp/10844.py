n = int(input())
dp = [[0 for i in range(10)] for i in range(100)]

for i in range(1, 10):
  dp[0][i] = 1

for i in range(1, 100):
  dp[i][0] = dp[i - 1][1]
  dp[i][1] = dp[i - 1][2] + dp[i - 1][0]
  dp[i][2] = dp[i - 1][3] + dp[i - 1][1]
  dp[i][3] = dp[i - 1][2] + dp[i - 1][4]
  dp[i][4] = dp[i - 1][3] + dp[i - 1][5]
  dp[i][5] = dp[i - 1][4] + dp[i - 1][6]
  dp[i][6] = dp[i - 1][5] + dp[i - 1][7]
  dp[i][7] = dp[i - 1][6] + dp[i - 1][8]
  dp[i][8] = dp[i - 1][7] + dp[i - 1][9]
  dp[i][9] = dp[i - 1][8]

print(sum(dp[n - 1]) % 1000000000)
salt = int(input())
dp = [-1 for i in range(0, salt + 1)]

dp[1] = -1
dp[2] = -1
dp[3] = 1

if salt >= 5:
  dp[5] = 1

for i in range(1, salt + 1):
  if dp[i] == -1:
    continue
  
  if i + 5 <= salt:
    dp[i + 5] = dp[i] + 1
  if i + 3 <= salt:
    if dp[i + 3] != -1:
      if dp[i + 3] > dp[i] + 1 > 3:
        dp[i + 3] = dp[i] + 1
    else:
      dp[i + 3] = dp [i] + 1



print(dp[salt])
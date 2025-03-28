N = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0 for i in range(101)]

for i in range(0, N):
  for j in reversed(range(L[i], 101)):
    dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(dp[99])
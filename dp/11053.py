n = int(input())
A = list(map(int, input().split()))
dp = [0 for i in range(n)]

dp[0] = 1

for i in range(1, n):
  arr = []
  for j in range(0, i):
    if A[j] < A[i]:
      arr.append(j)
  
  if len(arr) == 0:
    dp[i] = 1  
  else:
    m = max(arr, key=lambda n: dp[n])
    dp[i] = dp[m] + 1

print(max(dp))

N, T = map(int, input().split())
KK = []
SS = []

for i in range(N):
  # K: 예상 공부 시간, S: 그 단원 배점
  K, S = map(int, input().split())
  KK.append(K)
  SS.append(S)
  
dp = [0 for i in range(T + 1)]

for i in range(N):
  for j in reversed(range(KK[i], T + 1)):
    dp[j] = max(dp[j], dp[j - KK[i]] + SS[i])

print(dp[T])
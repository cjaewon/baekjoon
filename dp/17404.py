import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

cost: list[list[int, int, int]] = [[0, 0, 0]] + [list(map(int, input().split())) for i in range(N)]
# r, g, b

min_val = float("inf")

# === calc first house painted by red ===
dp = [[0, 0, 0] for i in range(N + 1)]

dp[1] = cost[1]
dp[2][0] = min(dp[1][1], dp[1][2]) + cost[2][0]
dp[2][1] = dp[1][2] + cost[2][1]
dp[2][2] = dp[1][1] + cost[2][2]

for i in range(3, N + 1):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

min_val = min(min_val, dp[N][0])

# === calc first house painted by green ===
dp = [[0, 0, 0] for i in range(N + 1)]

dp[1] = cost[1]
dp[2][0] = dp[1][2] + cost[2][0]
dp[2][1] = min(dp[1][0], dp[1][2]) + cost[2][1]
dp[2][2] = dp[1][0] + cost[2][2]

for i in range(3, N + 1):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

min_val = min(min_val, dp[N][1])

# === calc first house painted by blue ===
dp = [[0, 0, 0] for i in range(N + 1)]

dp[1] = cost[1]
dp[2][0] = dp[1][1] + cost[2][0]
dp[2][1] = dp[1][0] + cost[2][1]
dp[2][2] = min(dp[1][0], dp[1][1]) + cost[2][2]

for i in range(3, N + 1):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

min_val = min(min_val, dp[N][2])

print(min_val)

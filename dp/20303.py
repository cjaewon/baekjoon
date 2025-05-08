import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))

parent = [i for i in range(N + 1)]
size = [1] * (N + 1)

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  
  return parent[x]

def union(x, y):
  rx, ry = find(x), find(y)

  if rx == ry:
    return
  
  if size[rx] > size[ry]:
    parent[ry] = rx
    size[rx] += size[ry]
    candy[rx] += candy[ry]
  else:
    parent[rx] = ry
    size[ry] += size[rx]
    candy[ry] += candy[rx]


for i in range(M):
  a, b = map(int, input().split())
  union(a, b)

group: dict[int, tuple[int, int]] = {}

for x in range(1, N + 1):
  rx = find(x)

  if rx not in group:
    group[rx] = (size[rx], candy[rx])

# 0-1 Knapsack
# dp[i][k], i : used, k: bullied kid count = max candy

dp_candy = [0] + [cd for _, cd in group.values()] 
dp_size = [0] + [sz for sz, _ in group.values()]

dp = [[0 for j in range(K + 1)] for i in range(len(group) + 1)]

for i in range(1, len(group) + 1):
  for j in range(1, K + 1):
    if j - dp_size[i] < 0:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - dp_size[i]] + dp_candy[i])

print(dp[len(group)][K - 1])
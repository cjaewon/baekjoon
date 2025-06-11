import sys
import math

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

# sparse table

K = 25

min_st = [[nums[j] for j in range(N)] for i in range(K + 1)]
max_st = [[nums[j] for j in range(N)] for i in range(K + 1)]

for i in range(1, K + 1):
  for j in range(N):
    if not (j + (1 << i) <= N):
      break

    min_st[i][j] = min(min_st[i - 1][j], min_st[i - 1][j + (1 << (i - 1))])
    max_st[i][j] = max(max_st[i - 1][j], max_st[i - 1][j + (1 << (i - 1))])

# query
for _ in range(M):
  L, R = map(lambda s: int(s) - 1, input().split())

  i = math.floor(math.log2(R - L + 1))

  query_min = min(min_st[i][L], min_st[i][R - 2 ** i + 1])
  query_max = max(max_st[i][L], max_st[i][R - 2 ** i + 1])

  print(query_min, query_max)
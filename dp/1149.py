n = int(input())
table = [[0, 0, 0] for i in range(n)]

cases = []

for i in range(n):
  cases.append(list(map(int, input().split())))

table[0][0] = cases[0][0]
table[0][1] = cases[0][1]
table[0][2] = cases[0][2]

for i in range(1, n):
  # 그리디와 비슷한 것 같다.
  table[i][0] = min(table[i - 1][1], table[i - 1][2]) + cases[i][0]
  table[i][1] = min(table[i - 1][0], table[i - 1][2]) + cases[i][1]
  table[i][2] = min(table[i - 1][0], table[i - 1][1]) + cases[i][2]

print(min(table[n - 1][0], table[n - 1][1], table[n - 1][2]))
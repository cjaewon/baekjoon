n = int(input())
table = [[0, 0, 0] for i in range(n)]
stairs = [int(input()) for i in range(n)]

if n == 1:
  print(stairs[0])
  exit()

table[0][1] = stairs[0]
table[1][1] = max(stairs[1], stairs[0])
table[1][2] = stairs[0] + stairs[1]


for i in range(2, n):
  table[i][1] = max(table[i - 2][1], table[i - 2][2]) + stairs[i]
  table[i][2] = table[i - 1][1] + stairs[i]

print(max(table[n - 1][1], table[n - 1][2]))
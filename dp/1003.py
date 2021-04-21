cases = [int(input()) for i in range(int(input()))]
table = [[0, 0] for i in range(max(cases) + 2)] # D[i] = i번째 피보나치를 구할 때 0과 1이 출력되는 횟수

table[0][0] = 1
table[1][1] = 1

for i in range(2, max(cases) + 1):
  table[i][0] = table[i - 1][0] + table[i - 2][0]
  table[i][1] = table[i - 1][1] + table[i - 2][1]

for c in cases:
  print(table[c][0], table[c][1])

table = [0 for i in range(12)]

table[0] = 0
table[1] = 1
table[2] = 2
table[3] = 4

for i in range(4, 12):
  table[i] = table[i - 1] + table[i - 2] + table[i - 3]

for i in range(int(input())):
  n = int(input())
  print(table[n])
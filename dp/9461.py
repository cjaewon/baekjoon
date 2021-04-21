table = [0 for i in range(100)]

table[0] = 1
table[1] = 1
table[2] = 1
table[3] = 2
table[4] = 2
table[5] = 3

for i in range(6, 100):
  table[i] = table[i - 1] + table[i - 5]

for i in range(int(input())):
  print(table[int(input()) - 1])
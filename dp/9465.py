def solve(data):
  table = [[data[0][0], data[1][0], 0]]

  for i in range(1, len(data[0])):
    table.append([0, 0, 0])
    table[i][0] = max(
      table[i - 1][1] + data[0][i], 
      table[i - 1][2] + data[0][i],
    )
    table[i][1] = max(
      table[i - 1][0] + data[1][i],
      table[i - 1][2] + data[1][i]
    )

    table[i][2] = max(table[i - 1][0], table[i - 1][1], table[i - 1][2])

  print(max(table[len(table) - 1]))

for i in range(int(input())):
  input()
  data = [list(map(int, input().split())), list(map(int, input().split()))]
  solve(data)
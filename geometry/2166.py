N = int(input())
coordinates = []

for i in range(N):
  x, y = map(int, input().split())

  coordinates.append((x, y))

coordinates.append(coordinates[0])

s = 0

for i in range(N):
  s += coordinates[i][0] * coordinates[i + 1][1] - coordinates[i + 1][0] * coordinates[i][1]

print(round(abs(s) / 2, 1))
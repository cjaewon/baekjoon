costs = []

for i in range(int(input())):
  costs.append(int(input()))

costs = sorted(costs, reverse=True)

if len(costs) < 3:
  print(sum(costs))

s = 0

for i in range(0, len(costs)):
  if (i + 1) % 3 != 0:
    s += costs[i]

print(s)
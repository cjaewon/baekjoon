n = int(input())
xset = list(map(int, input().split()))
sortedxset = sorted((set(xset)))
xsetdict = { x: i for i, x in enumerate(sortedxset) } 

for x in xset:
  print(xsetdict[x], end=" ")
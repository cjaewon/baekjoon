N = int(input())
buildings = list(map(int, input().split()))

mstack = []
rec_buildings = []

for i, b in enumerate(buildings):
  while mstack:
    if b > buildings[mstack[-1]]:
      mstack.pop()
    else:
      break
      
  rec_buildings.append(mstack[-1] if mstack else -1)
  mstack.append(i)

print(" ".join(map(lambda x: str(x + 1), rec_buildings)))
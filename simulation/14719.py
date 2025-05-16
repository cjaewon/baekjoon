H, W = map(int, input().split())
heights = list(map(int, input().split()))

water = 0

for h in range(0, H + 1):
  ctx2 = 0
  ctx = "c"

  for x in range(W):
    if h <= heights[x]: # curr: black
      water += ctx2
      ctx2 = 0
      ctx = "c"

      if x + 1 < W and h > heights[x + 1]:
        ctx = "o"
    else: # curr: white
      if ctx == "o":
        ctx2 += 1

print(water)
N, M = map(int, input().split())
trees = list(map(int, input().split()))

def calcSum(trees, standard: int) -> int:
  s = 0
  
  for tree in trees:
    if tree < standard:
      continue
    else:
      s += tree - standard
  
  return s

start = 0
end = 2_000_000_000

max_height = 0

while start <= end:
  mid = (start + end) // 2

  s = calcSum(trees, mid)

  if s < M:
    end = mid - 1
  elif s > M:
    max_height = mid
    start = mid + 1
  else:
    max_height = mid
    break

print(max_height)
import sys
from collections import defaultdict

n = int(input())

for i in range(n):
  soldier_count, *soldiers = map(int, sys.stdin.readline().split())
  
  count = defaultdict(int)

  for soldier in soldiers:
    count[soldier] += 1

  for k, v in count.items():
    if soldier_count / 2 < v:
      print(k)
      break
  else:
    print("SYJKGW")

  
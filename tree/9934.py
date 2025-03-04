K = int(input()) # K: 깊이
building_sequence = list(map(int, input().split()))

pbt = [0 for i in range(2 ** K)] # 배열을 통해서 perfect binary tree를 구현하자.
index = 1

while pbt[-1] == 0:
  if index * 2 < 2 ** K:
    if pbt[index * 2] == 0:
      index = index * 2
    else:
      if pbt[index] == 0:
        pbt[index] = building_sequence.pop(0)
      else:
        if index * 2 + 1 < 2 ** K and pbt[index * 2 + 1] == 0:
          index = index * 2 + 1
        else:
          index = index // 2
  else:
    if pbt[index] == 0:
      pbt[index] = building_sequence.pop(0)
    else:
      if index * 2 + 1 < 2 ** K and pbt[index * 2 + 1] == 0:
        index = index * 2 + 1
      else:
        index = index // 2

pbt.pop(0)
for i in range(K):
  for j in range(2 ** i):
    print(pbt.pop(0), end=" ")
  print("")